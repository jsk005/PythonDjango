# account/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, logout
from account.forms import SignUpForm, LoginForm
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .RSACipher import *

def register_view(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated:
		return HttpResponse("You are already authenticated as " + str(user.email))

	context = {}
	if request.POST:
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(username=username, password=raw_password)
			login(request, account)
			destination = get_redirect_if_exists(request)
			if destination: # if destination != None
				return redirect(destination)
			return redirect('home')
		else:
			context['signup_form'] = form
	else:
		form = SignUpForm()
		context['signup_form'] = form

	return render(request, 'account/register.html', context)


def login_view(request, *args, **kwargs):
	context = {}

	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			# print(form.cleaned_data.get("username"))
			username = request.POST.get('username')
			enc_password = request.POST.get("password")
			password = RSACipher().decrypt(enc_password)
			user = authenticate(username=username, password=password)
			if user:
				# print(3)
				login(request, user)
				context['data'] = '1'
				context['message'] = '로그인 되었습니다.'
				return JsonResponse(context)
			else:
				# print(4)
				context['data'] = '0'
				context['message'] = '입력 정보를 확인하세요.'
				return JsonResponse(context)
		else:
			# print(2)
			context['data'] = '0'
			context['message'] = '입력 정보를 확인하세요.'
			return JsonResponse(context)
	else:
		form = LoginForm()
		context['form'] = form

	return render(request, "account/login.html", {'form':form})

def logout_view(request):
	logout(request)
	return redirect("home")


def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect

