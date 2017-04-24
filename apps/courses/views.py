# _*_encoding:utf-8_*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from operation.models import UserFavorite

from .models import Course


# Create your views here.


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        # 用于展示在右侧热门区域的几门课程(只取前三个)
        hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        # 用户选择的排序方式,注意筛选功能一定要写在分页之前
        # 因为分页只是对筛选结果进行合理展示,如果将分页写在前面则会失效
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_nums")
        
        
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        # 5是必修给的参数,代表每页显示的数量
        p = Paginator(all_courses, 6, request=request)

        courses = p.page(page)

        return render(request, 'course-list.html', {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_courses
        })


class CourseDetailView(View):
    """
    课程详情页
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 每当用户点击该课程自动增加课程点击数
        course.click_nums += 1
        course.save()

        has_fav_course = False
        has_fav_org = False

        # 检测该用户是否登录
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True

            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True


        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            # 如果不存在,就将其置为空数组
            relate_courses = []
        return render(request, "course-detail.html", {
            "course": course,
            "relate_courses": relate_courses,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org
        })


class CourseInfoView(View):
    """
    课程章节信息
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        return render(request, "course-video.html", {
            "course": course,
        })
