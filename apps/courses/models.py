# _*_encoding:utf-8_*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from orgnization.models import CourseOrg

# Create your models here.


class Course(models.Model):
    # 一般出现这种新增外键的情况都将null设置为True,因为新增的用户完整性约束会与已有数据产生冲突
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(verbose_name=u"难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")),
                              max_length=2)
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟)")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"课程封面", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    # 课程类别2017/4/23/1:03添加
    category = models.CharField(default=u"实战项目开发", max_length=20, verbose_name=u"课程类别")
    # 课程标签2017/4/23/1:34添加
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=10)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        #获取课程章节数
        return self.lesson_set.all().count()

    def get_learn_users(self):
        # 反向获取学习了这门课的前5个用户
        return self.usercourse_set.all()[:5]

    def __unicode__(self):
        return self.name


# 自然逻辑上,Lesson属于Course
# 此处,Lesson与Course属于多对一的关系
class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    """
    课程资源,例如ppt、代码之类的东西
    """
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name
