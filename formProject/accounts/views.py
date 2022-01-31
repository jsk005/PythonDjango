from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm

@csrf_exempt
def register(request, *args, **kwargs):
    user = request.user
    context = {}

    if user.is_authenticated:
        # return HttpResponse("You are already authenticated as " + str(user.email))
        return render(request,'home.html',context)

    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            # form.save()
            account = User.objects.create_user(**form.cleaned_data)
            login(request, account)
            # return render(request, 'home.html', context)
            context['data'] = '1'
            context['message'] = '회원 가입 완료'
            return JsonResponse(context)
        else:
            context['data'] = '0'  # 기존 가입된 회원
            context['message'] = '이미 가입된 회원입니다'
            return JsonResponse(context)
    else:
        form = UserForm()
        context['form'] = form

    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect("home")

