# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUpForm, LoginForm
from .RSACipher import *


@csrf_exempt
def register(request, *args, **kwargs):
    user = request.user
    context = {}

    if user.is_authenticated:
        # return HttpResponse("You are already authenticated as " + str(user.email))
        return render(request,'home.html',context)

    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # return render(request, 'home.html', context)
            context['data'] = '1'
            context['message'] = '회원 가입 완료'
            return JsonResponse(context)
        else:
            context['data'] = '0'  # 기존 가입된 회원
            context['message'] = '이미 가입된 회원입니다'
            return JsonResponse(context)
    else:
        form = SignUpForm()
        context['form'] = form

    return render(request, 'accounts/register.html', context)


def login_view(request):
    context = {}

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # 유효성 검사, 내부적으로 form.clean()을 실행한다.
            username = form.cleaned_data.get("username")
            enc_password = form.cleaned_data.get("password")
            password = RSACipher().decrypt(enc_password)

            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):
                    access = authenticate(username=username, password=password)
                    login(request, access)
                    context['data'] = '1'
                    context['message'] = '로그인 되었습니다.'
                else:
                    context['data'] = '0'
                    context['message'] = '입력 정보를 확인하세요.'
                    # context['message'] = '비밀번호가 다릅니다.'
                return JsonResponse(context)
            except User.DoesNotExist:  # 대문자 User 임에 주의
                # 가입된 회원인지 미가입된 회원인지 알 수 없는 메시지 출력이 중요
                context['data'] = '0'
                context['message'] = '입력 정보를 확인하세요.'
                return JsonResponse(context)
        else:
            context['form'] = form
    else:
        form = LoginForm()
        context['form'] = form

    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")

