# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from myapp.models import *
from django.contrib.auth.hashers import make_password


def index(request):

	gl=list(Guide.objects.order_by('-post_time')[:4].values())
	hl = list(Hotel.objects.order_by('id')[:6].values())
	sl = list(Scenic.objects.order_by('id')[:6].values())

	return render(request, 'index.html',{'gl':gl, 'hl': hl,'sl':sl})



	
def sign_in(request):
	if request.method== 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user:
			auth_login(request, user)
			return redirect('/')
		else:
			return render(request, 'login.html', {'wrong':'<script>alert(登录失败，用户名或密码不正确);</script>'})

	return render(request, 'login.html')
	
def sign_up(request):
	if request.method== 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		c_password = request.POST.get('c_password')
		if password!= c_password:
			return render(request, 'register.html', {'wrong':'两次密码不一致，请检查'})
		else:
			try:
				user = Member.objects.create(username=username,password= make_password(password))
				user.save()
				# Member.objects.create(username=username)
				return render(request, 'register.html', {'wrong':'用户注册成功'})
			except Exception as e:
				return render(request, 'register.html', { 'wrong':e})

			
	return render(request, 'register.html')

def search(request):
	kw=request.POST.get('kw')
	hs=Hotel.objects.filter(title__contains=kw)
	sc=Scenic.objects.filter(name__contains=kw)
	# print(hs,sc)
	return render(request, 'results.html',{'hs':hs,'sc':sc})
	
def comment(request):
    if request.method=="POST":
        if request.user.is_superuser:
            return HttpResponse('<script type="text/javascript">alert("管理员无法进行此操作!");</script>')
        if not request.user.id:
            return HttpResponse('<script type="text/javascript">alert("请先登录!");window.location.href="/login/";</script>')
        sid=request.POST.get('sid')
        hid=request.POST.get('hid')         
        user=Member.objects.get(id=request.user.id)
        content=request.POST.get('content')
        if sid:
            Comments.objects.create(user=user,sid=int(sid),ctype=0,content=content)
        else:
        	Comments.objects.create(user=user,sid=int(hid),ctype=1,content=content)
        return  HttpResponse('<script type="text/javascript">alert("留言成功!");window.location.href="/";</script>')


# def changePwd(request):
#     if request.method== 'POST':
#         cpwd_form = ChangePwd(request.POST)
#         if cpwd_form.is_valid():
#             username = cpwd_form.cleaned_data['username']
#             old_password = cpwd_form.cleaned_data['old_password']
#             new_password = cpwd_form.cleaned_data['new_password']

#             user = authenticate(username=username, password=old_password)
#             if user:
#                 user.set_password(new_password)
#                 user.save()
#                 return HttpResponse('修改密码成功')
#             else:
#                 return HttpResponse('原密码不正确，请检查后再试')
#         else:
#             return HttpResponse('更改密码失败，请稍后重试')
			
#     return HttpResponse('更改密码失败，请求方式不正确')

def sign_out(request):
	logout(request)
	return redirect('/login')

@login_required
def members(request):
	m=Member.objects.get(id=request.user.id)
	orders=Order.objects.filter(userId=m)
	goods=[ Scenic.objects.get(id=item.itemId) if item.otype==1 else Hotel.objects.get(id=item.itemId) for item in orders]
	if len(orders)==1:
		data=(orders,goods)
	else:
		data=zip(orders,goods)
	return render(request,'members.html',{'m':m,'data':data})


def scenic(request):
	slist=Scenic.objects.all()
	return render(request, 'scenic.html', {"slist":slist})



@login_required
def account(request):
	if request.method=="POST":
		res=Member.objects.get(id=request.user.id)
		res.phone=request.POST.get('phone')
		res.address=request.POST.get('address')
		res.intro=request.POST.get('intro')
		res.save()
		return redirect('/members')
	else:
		profile=Member.objects.get(id=request.user.id)
		return render(request,'account.html',{'p':profile})

def hotel(request):
	hs=Hotel.objects.all()
	return render(request, 'hotel.html', {'hs':hs})

def guide(request):
	gs=Guide.objects.all()
	return render(request, 'guide.html', {'gs':gs})

def article(request,id):
	aid= id if id else 1
	gs=Guide.objects.get(id=aid)
	return render(request, 'article.html', {'gs':gs})

def detail(request,id):
	hid= id if id else 1
	h=Hotel.objects.get(id=hid)
	cms=Comments.objects.filter(ctype=1,id=hid)
	return render(request, 'detail.html', {'h':h,'cms':cms})
def item(request,id):
	sid= id if id else 1
	s=Scenic.objects.get(id=sid)
	cms=Comments.objects.filter(ctype=0,id=sid)
	return render(request, 'item.html', {'s':s,'cms':cms})

@login_required
def publish(request):
	if request.method== 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		m=Member.objects.get(id=request.POST.get('uid'))
		g=Guide.objects.create(title=title,userId=m,content=content)
		g.save()
		return HttpResponse('发布成功！！')
	else:
		return render(request, 'publish.html')

# def books(request, id):
#     book_info = list(book.objects.filter(id=int(id)).values())
#     return render(request, 'book.html', {'book': book_info[0]})

@login_required
def order(request):
	uid = request.GET.get('uid')
	user=Member.objects.get(id=uid)
	t= request.GET.get('t')
	if t=="h":
		hid=request.GET.get('hid')
		hotel=Hotel.objects.get(id=hid)
		try:
			rec = Order.objects.create(userId=user,itemId=int(hid),otype=2,price=hotel.price)
			rec.save()
			return HttpResponse('提交订单成功！')
		except:
			return HttpResponse('提交订单失败！')
	else:
		sid=request.GET.get('sid')
		scenic=Scenic.objects.get(id=sid)
		try:
			rec = Order.objects.create(userId=user,itemId=int(sid),otype=1,price=scenic.price)
			rec.save()
			return HttpResponse('提交订单成功！')
		except:
			return HttpResponse('提交订单失败！')

# @login_required
# def remove(request):
#     if request.method== 'POST':
#         username = request.POST.get('username')
#         b_id = request.POST.get('id')

#         try:
#             user = infer.objects.get(username=username)
#             fav_book = book.objects.get(id=int(b_id))
#             user.fav.remove(fav_book)
#             return HttpResponse('移除图书成功')
#         except:
#             return HttpResponse('移除失败')
		
#     return HttpResponse('收藏失败，系统出错')
