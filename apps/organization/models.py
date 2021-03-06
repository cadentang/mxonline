# -*- coding:utf-8 -*-
from datetime import datetime

from django.db import models

# Create your models here.

class CityDict(models.Model):
	name = models.CharField(max_length=50,verbose_name="城市名称")
	desc = models.CharField(max_length=200,verbose_name="城市描述")
	add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

	class Meta:
		verbose_name = "城市"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class CourseOrg(models.Model):
	city = models.ForeignKey(CityDict,verbose_name="城市")
	name = models.CharField(max_length=50,verbose_name="机构名称")
	desc = models.TextField(verbose_name="机构描述")
	click_nums = models.IntegerField(default=0,verbose_name="点击数")
	fav_nums = models.IntegerField(default=0,verbose_name="收藏人数")
	image = models.ImageField(upload_to="org/%Y/%m", verbose_name= "封面图")
	address = models.CharField(max_length=150,verbose_name="机构地址")
	add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

	class Meta:
		verbose_name = "课程机构"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class Teacher(models.Model):
	name = models.CharField(max_length=50, verbose_name="教师名称")
	org = models.ForeignKey(CourseOrg, verbose_name="机构名称")
	work_years = models.IntegerField(default=0,verbose_name="工作年限")
	work_company = models.CharField(max_length=50, verbose_name="就职公司")
	work_position = models.CharField(max_length=50,verbose_name="就职职位")
	points  = models.CharField(max_length=50,verbose_name="教学特点")
	click_nums = models.IntegerField(default=0,verbose_name="点击数")
	fav_nums = models.IntegerField(default=0,verbose_name="收藏数")
	add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

	class Meta:
		verbose_name = "教师"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name
