# accounts forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import authenticate
from .RSACipher import *


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='userID',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "아이디를 입력하세요",
                "class": "form-control"
            }
        ))

    name = forms.CharField(
        label='userNM',
        widget=forms.TextInput(
            attrs={
                "placeholder": "성명을 입력하세요",
                "class": "form-control"
            }
        ))

    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "이메일을 입력하세요",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'name', 'email')  # 폼을 만들 때 사용할 필드를 정의


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

    # jQuery ajax 처리보다 def clean(self)가 먼저 동작되어 코드 삭제했음.

class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=32, label='userID',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("입력 정보를 확인하세요.")

