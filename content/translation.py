from modeltranslation.translator import register, TranslationOptions
from rest_framework.views import APIView

from .models import *


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ("title", "title", "description", "summary", "body")


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ("title", "description")
