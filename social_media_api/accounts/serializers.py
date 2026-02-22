# accounts/serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

# Serializer for user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ensures password is not returned
    token = serializers.CharField(read_only=True)  # token will be returned after creation

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'token')

    def create(self, validated_data):
        # create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        # create a token for the new user
        token = Token.objects.create(user=user)
        user.token = token.key
        return user

# Serializer for login
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)