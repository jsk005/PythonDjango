from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','useremail','password','created_at','updated_at')
    search_fields = ['username']

admin.site.register(User, UserAdmin)