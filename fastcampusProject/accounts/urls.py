# app urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # path('register/', views.register, name='ajax_register'), # ajax_register
    path('register/', views.UserRegisterView.as_view(), name='ajax_register'), # ajax_register

    # path('login/', views.login, name='ajax_login'),
    path('login/', views.UserLoginView.as_view(), name='ajax_login'),

    # path('logout/',views.logout),
    path('logout/',views.UserLogoutView.as_view()),
]