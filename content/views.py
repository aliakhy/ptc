from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from unicodedata import lookup
from .serializers import *
from content.models import Project,Blog




class ProjectView(
    ListModelMixin,
    RetrieveModelMixin,
    GenericAPIView):
    queryset = Project.objects.select_related('category').prefetch_related('gallery').all()

    def get_serializer_class(self):
        if  self.kwargs.get('slug'):
            return ProjectDetailSerializer
        return ProjectListSerializer

    lookup_field = 'slug'
    def get(self, request, slug=None):
        if slug:
            return self.retrieve(request, slug=slug)
        return self.list(request)


class BlogView(
    ListModelMixin,
    RetrieveModelMixin,
    GenericAPIView):
    queryset = Blog.objects.filter(is_show=True)

    def get_serializer_class(self):
        if self.kwargs.get('slug'):
            return BlogDetailSerializer
        return BlogListSerializer

    lookup_field = 'slug'

    def get(self, request, slug=None):
        if slug:
            return self.retrieve(request, slug=slug)
        return self.list(request)


