from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


# Register your models here.
@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ("id", "title", "slug", "is_show", "created_at")
    list_filter = ("created_at", "is_show")
    search_fields = ("title",)
    list_editable = ("is_show",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "blog__title", "created_at")
    search_fields = ("blog__title",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "project__title")


class GalleryInline(admin.TabularInline):
    model = Gallery
    autocomplete_fields = ("project",)
    extra = 0


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ("id", "title", "slug", "category", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("title",)
    inlines = [GalleryInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "created_at")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("company_name", "email", "created_at")
    list_filter = ("company_name", "created_at")
    search_fields = ("company_name",)


@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "created_at",
        "education_degree",
    )
    list_filter = ("first_name", "status", "education_level")

@admin.register(History)
class HistoryAdmin(TranslationAdmin):
    list_display = (
        "id",
        "year"
    )
    list_filter = ("year",)
