from django.shortcuts import render
from django.http import HttpResponse

def home(request, *args, **kwargs):
	return render(request, 'user.html',{})

def user(request, *args, **kwargs):
	return render(request, 'user.html',{})

def admin(request, *args, **kwargs):
	return render(request, 'admin.html',{})
