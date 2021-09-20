from django.contrib import admin
from . models import UserMetas

# Register your models here.

class UserMetasAdmin(admin.ModelAdmin):
    list_display = ('name','email','designation')
    search_fields = ['name']

admin.site.register(UserMetas,UserMetasAdmin)