from django import forms
from django.contrib.auth.hashers import check_password
from .models import User

class RegisterForm(forms.Form):
    useremail = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    repasswd = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()
        useremail = cleaned_data.get('useremail')
        password = cleaned_data.get('password')
        repasswd = cleaned_data.get('re_password')

        if password and repasswd:
            if password != repasswd:
                self.add_error('password', '비밀번호가 서로 다릅니다.')


class LoginForm(forms.Form):
    useremail = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.Textarea, label='비밀번호'
        # widget = forms.PasswordInput, label = '비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        useremail = cleaned_data.get('useremail')
        password = cleaned_data.get('password')

        if useremail and password:
            try:
                user = User.objects.get(useremail=useremail)
            except User.DoesNotExist:
                self.add_error('useremail', '존재하지 않는 아이디 입니다')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 다릅니다')
