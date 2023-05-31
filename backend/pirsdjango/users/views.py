from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login , logout

from .serializers import UserSerializer
from .models import User
from userprofile.models import Profile
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    authentication_classes = []
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        profile = Profile.objects.create(user=user)
        profile.save()

        token = Token.objects.create(user=user)
        

        return Response({'token': token.key})

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response('Invalid credentials', status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    def post(self, request):
        logout(request)
        return Response('User Logged out successfully')
