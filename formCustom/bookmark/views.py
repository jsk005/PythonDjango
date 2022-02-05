from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

class BookmarkLV(LoginRequiredMixin,ListView):
    model = Bookmark
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class BookmarkDV(DetailView):
    model = Bookmark

