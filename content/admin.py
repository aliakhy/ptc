from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog__title', 'created_at','updated_at')
    search_fields = ('blog__title',)



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'project__title')


class GalleryInline(admin.TabularInline):
    model = Gallery
    autocomplete_fields = ('project',)
    extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category','created_at','is_show')
    list_editable = ('is_show',)
    list_filter = ('is_show','category','created_at')
    search_fields = ('title',)
    inlines = [GalleryInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

