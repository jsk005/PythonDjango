# project urls.py
from django.contrib import admin
from django.urls import path
from accounts import views
from .views import homescreen_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homescreen_view, name='home'),
    path('signup/', views.register, name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
