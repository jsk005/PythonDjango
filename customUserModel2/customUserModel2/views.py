# project views.py
from django.shortcuts import render
from django.conf import settings

def homescreen_view(request):
	context = {}
	return render(request, "home.html", context)

