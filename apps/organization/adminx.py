__author__ = 'caden'
__data__ = ' 10:41'

import  xadmin
from .models import CityDict, CourseOrg, Teacher

class CityDictAdmin(object):
	list_display = ['name', 'desc', 'add_time']
	search_fields = ['name', 'desc']
	list_filter = ['name', 'desc', 'add_time']

class CourseOrgAdmin(object):
	list_display = ['city', 'name', 'desc','click_nums','fav_nums','image','address','add_time']
	search_fields = ['city', 'name', 'desc','click_nums','fav_nums','address']
	list_filter = ['city__name', 'name', 'desc','click_nums','fav_nums','image','address','add_time']

class TeacherAdmin(object):
	list_display = ['name', 'org', 'work_years','work_company','work_position','points','click_nums','fav_nums','add_time']
	search_fields = ['name', 'org', 'work_years','work_company','work_position','points']
	list_filter = ['name', 'org', 'work_years','work_company','work_position','points','click_nums','fav_nums','add_time']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
