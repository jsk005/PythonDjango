from django.shortcuts import render
from django.conf import settings

DEBUG = False

def home_screen_view(request):
	context = {}
	context['debug_mode'] = settings.DEBUG
	context['debug'] = DEBUG
	return render(request, "home.html", context)

