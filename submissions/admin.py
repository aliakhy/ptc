from django.contrib import admin

from content.models import Gallery
from .models import *

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email', 'created_at')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'created_at')
    list_filter = ('company_name', 'created_at')
    search_fields = ('company_name',)

@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at','education_degree')
    list_filter = ('first_name', 'status', 'education_level')
