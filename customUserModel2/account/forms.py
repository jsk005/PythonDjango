# account/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User
from .RSACipher import *

# 회원 가입 폼
class SignUpForm(UserCreationForm):
	username = forms.CharField(
		label='userID',
		widget=forms.TextInput(
			attrs={
				"placeholder": "Username",
				"class": "form-control"
			}
		))

	email = forms.EmailField(
		label='email',
		widget=forms.EmailInput(
			attrs={
				"placeholder": "Email",
				"class": "form-control"
			}
		))

	class Meta:
		model = User
		fields = ('username', 'name', 'email', 'password1', 'password2', )

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = User.objects.get(username=username)
		except Exception as e:
			return username
		raise forms.ValidationError(f"UserID {username} is already in use.")

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = User.objects.get(email=email)
		except Exception as e:
			return email
		raise forms.ValidationError(f"Email {email} is already in use.")


# 로그인 인증 폼
class LoginForm(forms.Form):
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
