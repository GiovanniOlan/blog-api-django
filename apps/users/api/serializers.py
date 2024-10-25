from rest_framework import serializers

from apps.users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user
