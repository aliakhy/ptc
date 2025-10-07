from modeltranslation.translator import register, TranslationOptions

from .models import Blog, Project, History


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ("title", "title", "description", "summary", "body")


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ("achievement",)
