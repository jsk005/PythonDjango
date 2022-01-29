# project urls.py
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from .views import home_screen_view
from account.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
    path('register/', register_view, name='register' ),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)