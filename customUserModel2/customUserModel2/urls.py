# project urls.py
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from .views import homescreen_view
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homescreen_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)