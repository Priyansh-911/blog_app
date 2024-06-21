from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=150)
#     password = serializers.CharField(write_only=True, required=True)
#
#     def validate(self, attr):
#         username = attr.get['username']
#         password = attr.get['password']
#
#         user = User.objects.filter(username=username).first()
#
#         if user is None:
#             raise serializers.ValidationError('User is not present in DB')
#
#         if not user.check_password(password):
#             raise serializers.ValidationError('Incorrect password: please try again')
#
#         refresh = RefreshToken.for_user(user)
#         attr['refresh'] = str(refresh)
#         attr['access'] = str(refresh.access_token)
#
#         return attr
