from rest_framework import status, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog, Like
from .serializer import BlogSerializer, LikeSerializer


class BlogPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class BlogViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        blogs = Blog.objects.all().order_by('-createdAt')
        paginator = BlogPagination()
        page = paginator.paginate_queryset(blogs, request)

        if page is not None:
            serializer = BlogSerializer(blogs, many=True)
            print(paginator.get_page_size(request))
            return paginator.get_paginated_response(serializer.data)

        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response({"msg": "Blog has been successfully created", "id": serializer.data['id']},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleViewBlogViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        serializer = BlogSerializer(blog)

        print(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)






class LikeViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, blog_id):
        # serializer = LikeSerializer(data=request.data)
        liked_blog = Blog.objects.get(id=blog_id)

        if Like.objects.filter(user=request.user, blog=liked_blog).exists():
            return Response({'detail': 'You have already liked this blog.'}, status=status.HTTP_400_BAD_REQUEST)

        like = Like(user=request.user, blog=liked_blog)
        like.save()

        return Response({'msg': "Blog liked successfully"}, status=status.HTTP_201_CREATED)

    def delete(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)

        try:
            like = Like.objects.get(user=request.user, blog=blog)

        except Like.DoesNotExist:
            return Response({'msg' : "user has not liked the post"}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"msg" : "Like have been removed successfully"}, status=status.HTTP_204_NO_CONTENT)