from django.urls import path
from apps.blog_reactions import views


urlpatterns = [
    path("likes/",views.Likes.as_view()),
]