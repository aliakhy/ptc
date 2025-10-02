from django.urls import path

from .views import *
# Create your tests here.
urlpatterns = [
    path('projects/', ProjectView.as_view()),
    path('projects/<slug:slug>/', ProjectView.as_view()),
    path('blog/', BlogView.as_view()),
    path('blog/<slug:slug>/', BlogView.as_view()),
]