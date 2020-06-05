from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # Make endpoint create a user & save password with django in-built set_password (which hashes it securely)
        user = UserModel.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        # Generate a persistent API Token for user. Token is retrieved on login, and can be regenerated at later time.
        Token.objects.get_or_create(user=user)
        return user

    class Meta:
        model = UserModel
        fields = ("id", "username", "password")
