# accounts forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=32, label='userID',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control"
            }
        ))

    # jQuery ajax 처리보다 먼저 동작되어 아래 코드는 주석처리했음.

    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')
    #
    #     if username and password:
    #         try:
    #             user = User.objects.get(username=username)
    #             if not check_password(password, user.password):
    #                 self.add_error('password', '비밀번호가 다릅니다.')
    #             else:
    #                 self.user_id = user.id
    #         except Exception:
    #             self.add_error('username', '존재하지 않는 아이디 입니다.')


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='userID',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email')

    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['minlength'] = 6
        self.fields['username'].widget.attrs['maxlength'] = 15
