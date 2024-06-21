from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializer import RegisterSerializer


class RegisterView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":RegisterSerializer(user, context=self.get_serializer_context()).data
        })


# class UserLoginView(generics.GenericAPIView):
#     serializer_class = UserLoginSerializer
