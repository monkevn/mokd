# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    address=models.CharField(max_length=200, blank=True)
    phone=models.CharField(max_length=11, blank=True)
    intro = models.TextField(u'简介',blank=True, null=True,)
    regtime=models.DateTimeField('注册时间', auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        pass

class Hotel(models.Model):
    title = models.CharField(max_length=200,blank=True,null = False,verbose_name=u'酒店名称')
    pic = models.ImageField(upload_to="static/upload/",verbose_name=u'图片')
    intro = models.TextField(verbose_name=u'简介')
    price = models.FloatField(verbose_name=u'价格', default=0)
    tel=models.CharField(max_length=20,blank=True,verbose_name=u'电话')
    address = models.CharField(max_length=50, blank=True, null=True,verbose_name=u'地址')

    def __str__(self):
        return self.title

class Order(models.Model):
    userId=models.ForeignKey(Member, blank=True, null=True, verbose_name='用户id')
    itemId=models.IntegerField('商品id', default=0)
    otype=models.IntegerField('商品类型', default=0)
    price=models.FloatField('价格', default=0)
    time=models.DateTimeField('生成时间', auto_now_add=True)

class Guide(models.Model):
    userId=models.ForeignKey(Member, blank=True, null=True, verbose_name='用户id')
    title = models.CharField(max_length=200,blank=True,null = False,verbose_name=u'标题')
    post_time = models.DateTimeField('发布时间', auto_now_add=True)
    content = models.TextField(u'内容')

    def __str__(self):
        return self.title

class Scenic(models.Model):
    name = models.CharField(max_length=200,blank=True,null = False,verbose_name=u'景点名称')
    pic = models.ImageField(upload_to="static/upload/",verbose_name=u'景点图片')
    price=models.FloatField(verbose_name=u'价格', default=0)
    intro = models.TextField(u'简介')
    address = models.CharField(max_length=200, blank=True, null=True,verbose_name=u'地址')

    def __str__(self):
        return self.name

class Comments(models.Model):
    sid = models.IntegerField(verbose_name='id',default=0 )
    ctype=models.IntegerField(default=0,verbose_name="类别")
    user=models.ForeignKey(Member, verbose_name='用户')
    content=models.TextField(verbose_name='简介' )
    addtime= models.DateTimeField(verbose_name='添加时间',auto_now_add=True)

    def __str__(self):
        return self.content
    class Meta:
        verbose_name = '好友'
        verbose_name_plural = verbose_name
        ordering = ['-id']