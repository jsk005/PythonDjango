# project urls.py
from django.contrib import admin
from django.urls import path, include
from accounts import views
from accounts.views import LoginView, UserLoginView
from .views import homescreen_view
from django.contrib.auth import views as auth_views
from bookmark.views import BookmarkLV, BookmarkDV


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homescreen_view, name='home'),
    path('signup/', views.register, name='signup'),
    # path('login/', views.login_view, name='login'),
    # path('login/', LoginView.as_view(), name='login'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # class-based views
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),

]
