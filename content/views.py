from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from unicodedata import lookup
from .serializers import *
from content.models import Project, Blog


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

    # lookup_field = 'slug'
    #
    # def get(self, request, slug=None):
    #     if slug:
    #         return self.retrieve(request, slug=slug)
    #     return self.list(request)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(
            blog__slug=self.kwargs["blog_slug"], status="Published"
        )


class ApplyView(CreateAPIView):
    serializer_class = ApplySerializer


class ContactView(CreateAPIView):
    serializer_class = ContactSerializer


class OrderView(CreateAPIView):
    serializer_class = OrderSerializer
