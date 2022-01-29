from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from .models import User

# Create your views here.
def index(reqest):
    user_id = reqest.session.get('user')

    if user_id:
        user = User.objects.get(pk=user_id)
        return HttpResponse(user.useremail)

    return redirect('/')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)

        res_data = {}
        try:
            user = User.objects.get(useremail=useremail)
            if check_password(password, user.password):
                # 비밀번호가 일치하면 세션 생성
                request.session['user'] = user.id
                res_data['data'] = '1'
                res_data['message'] = '로그인 되었습니다.'
            else:
                res_data['data'] = '0'
                res_data['message'] = '입력 정보를 확인하세요.'
            return JsonResponse(res_data)
        except User.DoesNotExist:
            # 대문자 User 임에 주의
            res_data['data'] = '0'
            res_data['message'] = '입력 정보를 확인하세요.'
            return JsonResponse(res_data)

        return render(request, 'login.html', res_data)



def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        useremail = request.POST.get('useremail',None)
        password = request.POST.get('password',None)

        res_data ={}
        try:
            user = User.objects.get(useremail=useremail)
            if user:
                res_data['status'] = '0' # 기존 가입된 회원
                return JsonResponse(res_data)
        except User.DoesNotExist:
            # 대문자 User 임에 주의
            user = User(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )
            user.save()
            # session 생성
            user = User.objects.get(useremail=useremail)
            request.session['user'] = user.id
            res_data['data'] = '1'
            res_data['message'] = '회원 가입 완료'
            return JsonResponse(res_data)

        return render(request,'register.html',res_data)


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/user/login')

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

class UserLogoutView(BaseView):
    def get(self, request):
        if self.request.session.get('user'):
            del (self.request.session['user'])
        return redirect('/')

class UserLoginView(BaseView):
    template_name = 'login.html'
    def post(self,request):
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)

        try:
            user = User.objects.get(useremail=useremail)
            if check_password(password, user.password):
                self.request.session['user'] = user.id  # 세션 생성
                data = '1'
                message = '로그인 되었습니다.'
            else:
                data = '0'
                message = '입력 정보를 확인해주세요.'
            return self.response(data, message, status='')
        except User.DoesNotExist:
            # 대문자 User 임에 주의
            data = '0'
            # message = '입력 정보를 확인해주세요.'  # 가입 여부를 모르게 동일한 메시지 출력이 중요
            message = '등록된 회원 정보가 없습니다.'
            return self.response(data, message, status='')
        return self.response()


class UserRegisterView(BaseView):
    template_name = 'register.html'
    def post(self,request):
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)

        if not username:
            return self.response(data='0', message='성명을 입력해주세요.', status=400)
        if not password:
            return self.response(data='0', message='패스워드를 입력해주세요.', status=400)
        try:
            validate_email(useremail)
        except ValidationError:
            return self.response(data='0', message='올바른 이메일을 입력해주세요.', status=400)

        try:
            user = User.objects.get(useremail=useremail)
            if user:
                return self.response(data='0', message='이미 가입된 아이디입니다.', status=400)
        except User.DoesNotExist:
            # 대문자 User 임에 주의
            user = User(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )
            user.save()
            # session 생성
            user = User.objects.get(useremail=useremail)
            self.request.session['user'] = user.id
            return self.response(data='1', message='회원 가입 완료.', status=200)

        return self.response({'user.id': user.id})





