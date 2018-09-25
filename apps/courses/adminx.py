__author__ = 'caden'
__data__ = ' 9:27'
import xadmin
from .models import Course,Lesson,Video,CourseResource


class CourseAdmin(object):

	list_display = ['name', 'desc', 'detail', 'degree', 'learn_times','students', 'fav_nums', 'click_nums']
	search_fields = ['name', 'desc', 'detail', 'degree', 'students']
	list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times','students', 'fav_nums', 'click_nums']

class LessonAdmin(object):

	list_display = ['course', 'name', 'add_time']
	search_fields = ['course', 'name']
	list_filter = ['course__name', 'name', 'add_time']#course是外键，需以这种方式显示

class VideoAdmin(object):

	list_display = ['lesson', 'name', 'add_time']
	search_fields = ['lesson', 'name']
	list_filter = ['lesson__name', 'name', 'add_time']

class CourseResourceAdmin(object):

	list_display = ['course', 'name', 'download','add_time']
	search_fields = ['course', 'name']
	list_filter = ['course__name', 'name', 'download','add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)


