from django.urls import path, include
from .views import BlogViewSet, LikeViewSet, SingleViewBlogViewSet


urlpatterns = [
    path("user/", include("user.urls")),
    path("blogs/", BlogViewSet.as_view(), name="give-blog-list"),
    path("blogs/<int:blog_id>/like/",  LikeViewSet.as_view(), name="create-like"),
    path("blogs/<int:blog_id>/",  SingleViewBlogViewSet.as_view(), name="like-count")
]
