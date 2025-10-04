from rest_framework import permissions
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.utils import translation
from unicodedata import lookup
from .serializers import *
from content.models import Project, Blog
from celery import Celery



class ProjectView(ListModelMixin, RetrieveModelMixin, GenericAPIView):
    queryset = (
        Project.objects.select_related("category").prefetch_related("gallery").all()
    )

    def get_serializer_class(self):
        if self.kwargs.get("slug"):
            return ProjectDetailSerializer
        return ProjectListSerializer

    lookup_field = "slug"

    def get(self, request, slug=None):
        if slug:
            return self.retrieve(request, slug=slug)
        return self.list(request)


class BlogViewSet(ReadOnlyModelViewSet):
    queryset = Blog.objects.filter(is_show=True)
    serializer_class = BlogListSerializer
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.kwargs.get("slug"):
            return BlogDetailSerializer
        return BlogListSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return CommentWriteSerializer
        return CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(
            blog__slug=self.kwargs["blog_slug"], status="published"
        )

    def get_permissions(self):
        if self.request.method in [permissions.SAFE_METHODS, "POST"]:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def perform_create(self, serializer):
        lang = translation.get_language()
        blog = Blog.objects.get(slug=self.kwargs["blog_slug"])
        serializer.save(language=lang, blog=blog)


class ApplyView(CreateAPIView):
    serializer_class = ApplySerializer


class ContactView(CreateAPIView):
    serializer_class = ContactSerializer


class OrderView(CreateAPIView):
    serializer_class = OrderSerializer
