from django.urls import path, include
from .views import BlogViewSet


urlpatterns = [
    path("user/", include("user.urls")),
    path("blogs/", BlogViewSet.as_view(), name="blog-list")
]
