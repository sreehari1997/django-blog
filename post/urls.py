from django.urls import path
from post.views import (
    BlogDetailView, BlogListView, create_post, edit_post, like_post
)

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('<int:pk>/detail/', BlogDetailView.as_view(), name="detail"),
    path('create/', create_post, name="create"),
    path('<int:pk>/edit/', edit_post, name="edit"),
    path('<int:pk>/like/', like_post, name="like"),
]
