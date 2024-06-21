from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializer import BlogSerializer


class BlogViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        blogs = Blog.objects.all().order_by('-createdAt')
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)