__author__ = 'caden'
__data__ = ' 23:31'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner

class BaseSetting(object):
	enable_themes = True
	use_bootswatch = True


class GlobalSetting(object):#全局配置
	site_title = "慕学后台管理系统" #后台管理标题
	site_footer = "慕学在线网"#底部信息
	menu_style = "accordion"#导航栏折叠

class EmailVerifyRecordAdmin(object):
	list_display = ['code', 'email', 'send_type', 'send_time']#后台系统展示的字段
	search_fields = ['code', 'email', 'send_type']#搜索的字段
	list_filter = ['code', 'email', 'send_type', 'send_time']#过滤的字段

class BannerAdmin(object):
	list_display = ['title', 'image', 'url', 'index', 'add_time']
	search_fields = ['title', 'image', 'url', 'index']
	list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)#注册信息，将表注册到后台管理系统中
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)