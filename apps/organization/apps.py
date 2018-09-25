
from django.apps import AppConfig
"""
该文件是应用自动创建的，verbose_name是后台管理系统中导航栏各数据表的名称
"""

class OrganizationConfig(AppConfig):
    name = 'organization'
    verbose_name = "课程机构"
