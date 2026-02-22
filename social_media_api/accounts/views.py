from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from .models import CustomUser
from rest_framework.views import APIView

# Registration View
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        response.data['token'] = str(refresh.access_token)
        return response

# Profile View (requires authentication)
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class RootView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Social Media API"})