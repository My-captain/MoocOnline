# _*_ encoding:utf-8_*_
# __author__ = 'Mr.Robot
# __date__ = '2017/04/09 20:23'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']


class TeacherAdmin(object):
    list_display = ['name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums',
                    'fav_nums', 'add_time']
    search_fields = ['name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
