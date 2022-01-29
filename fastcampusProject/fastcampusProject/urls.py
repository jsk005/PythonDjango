from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.HomeView.as_view(), name='index'),
    path('user/', include('accounts.urls')),
]
