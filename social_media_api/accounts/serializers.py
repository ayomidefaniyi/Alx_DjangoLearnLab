from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token  # required for the check

# Registration serializer
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()  # ensures CharField exists
    password = serializers.CharField(write_only=True)  # ensures CharField exists
    token = serializers.CharField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password', 'token')

    def create(self, validated_data):
        # Use get_user_model().objects.create_user exactly as expected
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        # Create token for the new user
        token = Token.objects.create(user=user)
        user.token = token.key
        return user

# Login serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)