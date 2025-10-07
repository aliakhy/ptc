from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from content.api.views import *

router = DefaultRouter()
router.register("blog", BlogViewSet, basename="blogs")
comment_router = routers.NestedDefaultRouter(router, "blog", lookup="blog")
comment_router.register("comments", CommentViewSet, basename="blog-comments")
router.register("projects", ProjectViewSet, basename="blog-project")
router.register("history", HistoryViewSet, basename="history")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(comment_router.urls)),
    path("membership/", ApplyView.as_view()),
    path("contact-us/", ContactView.as_view()),
    path("how-to-create/", OrderView.as_view()),
]
