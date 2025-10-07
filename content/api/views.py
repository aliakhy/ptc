from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from content.api.serializers import *
from content.models import Project, Blog,History
from rest_framework.response import Response



class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = (
        Project.objects.select_related("category")
        .prefetch_related("gallery")
        .order_by("-created_at")
        .all()
    )
    serializer_class = ProjectSerializer

    lookup_field = "slug"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["list_view"] = self.action == "list"
        return context


class BlogViewSet(ReadOnlyModelViewSet):
    queryset = Blog.objects.filter(is_show=True).order_by("-created_at").all()
    serializer_class = BlogSerializer
    lookup_field = "slug"

    def get_serializer_context(self):
        if self.action == "list":
            return {"list_view": True}
        else:
            return {"list_view": False}


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return CommentWriteSerializer
        return CommentSerializer

    def get_queryset(self):
        return (
            Comment.objects.filter(
                blog__slug=self.kwargs["blog_slug"], status="published"
            )
            .order_by("-created_at")
            .all()
        )

    def get_permissions(self):
        if self.request.method in ["GET", "POST"]:
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

class HistoryViewSet(ReadOnlyModelViewSet):
    serializer_class = HistorySerializer
    queryset = History.objects.all().order_by("-created_at")
    def retrieve(self, request, *args, **kwargs):
        return Response({'detail': 'Method "Get" not allowed'},
            status=status.HTTP_405_METHOD_NOT_ALLOWED)