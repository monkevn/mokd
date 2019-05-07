# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *



# class MemberAdmin(admin.ModelAdmin):
# 	fields=('title','author','intro','bid','tags','pic')
# 	list_display = ('id','title','author',)
# 	list_display_links = ('id','title',)

# class HotelAdmin(admin.ModelAdmin):
# 	fields=('username',)
# 	list_display = ('id','username','regtime')
# 	list_display_links = ('id','username',)

# class GuideAdmin(admin.ModelAdmin):
# 	fields=('book','user','mark')
# 	list_display = ('id','book','user',)
# 	list_display_links = ('id','book','user',)

# class ScenicAdmin(admin.ModelAdmin):
# 	fields=('book','user','mark')
# 	list_display = ('id','book','user',)
# 	list_display_links = ('id','book','user',)



admin.site.register(Member)
admin.site.register(Hotel)
admin.site.register(Order)
admin.site.register(Guide)
admin.site.register(Scenic)