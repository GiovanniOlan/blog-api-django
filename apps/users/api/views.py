from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.api.serializers import (
    UserRegisterSerializer,
    UserSerializer,
    UserUpdateSerializer,
)


class RegisterView(APIView):
    def post(self, request):
        userSerializer = UserRegisterSerializer(data=request.data)

        if not userSerializer.is_valid():
            return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        userSerializer.save()
        return Response(userSerializer.data, status=status.HTTP_201_CREATED)


class LoggedUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = UserSerializer(request.user)
        return Response(user.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = User.objects.get(pk=request.user.pk)
        user_serializer = UserUpdateSerializer(user, data=request.data)
        if not user_serializer.is_valid():
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_200_OK)
