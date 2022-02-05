# accounts/views.py
from django.conf import settings
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth.views import SuccessURLAllowedHostsMixin
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, resolve_url
from .forms import SignUpForm, LoginForm, UserLoginForm
from .RSACipher import *
from .models import User
# from django.contrib.auth.models import User


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


def login_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    next_page = get_redirect_if_exists(request)
    context = {}

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data.get("username"))
            username = request.POST.get("username")
            enc_password = request.POST.get("password")
            password = RSACipher().decrypt(enc_password)

            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request,user)
                context['data'] = '1'
                context['message'] = '로그인 되었습니다.'
                context['nexturl'] = next_page
                return JsonResponse(context)
            else:
                context['data'] = '0'
                context['message'] = '입력 정보를 확인하세요.'
                return JsonResponse(context)
        else:
            print(2)
            context['data'] = '0'
            context['message'] = '입력 정보를 확인하세요.'
            return JsonResponse(context)
    else:
        form = LoginForm()
        context['form'] = form

    return render(request, "accounts/login.html", {'form':form})

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect


@method_decorator(csrf_exempt, name='dispatch')
class BaseView(TemplateView):
    @staticmethod
    def response(data={}, message='', status=200):
        result = {
            'data': data,
            'message': message,
            'status': status,
        }
        return JsonResponse(result)

class LoginView(TemplateView):

    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        if self.request.GET.get("redirect_to"):
            redirect_to = str(self.request.GET.get("redirect_to"))
            self.request.session['redirect_to'] = redirect_to
        return render(request,'accounts/login.html',context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            enc_password = request.POST.get("password")
            password = RSACipher().decrypt(enc_password)
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                context['data'] = '1'
                context['message'] = '로그인 되었습니다.'
                context['nexturl'] = self.request.session.get('redirect_to')
                return JsonResponse(context)
            else:
                context['data'] = '0'
                context['message'] = '입력 정보를 확인하세요.'
                return JsonResponse(context)
        else:
            context['data'] = '0'
            context['message'] = '입력 정보를 확인하세요.'
            return JsonResponse(context)


class UserLoginView(FormView):
    template_name = 'accounts/userlogin.html'
    form_class = UserLoginForm
    # success_url = reverse_lazy("home")

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None and user.is_active:
            login(self.request,user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get("redirect_to"):
            redirect_to = self.request.GET.get("redirect_to")
            self.request.session['redirect_to'] = redirect_to
        return context

    def get_success_url(self):
        url = self.request.session.get('redirect_to')
        return url or resolve_url(settings.LOGIN_REDIRECT_URL)


