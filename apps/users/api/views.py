from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.users.models import User
from apps.users.api.serializers import UserRegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        userSerializer = UserRegisterSerializer(data=request.data)

        if not userSerializer.is_valid():
            return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        userSerializer.save()
        return Response(userSerializer.data, status=status.HTTP_201_CREATED)
