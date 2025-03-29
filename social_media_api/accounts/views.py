from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import UserSerializer, RegisterSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model
from .models import CustomUser


User = get_user_model()
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': response.data})


class LoginView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer] 
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': {"username": user.username, "email": user.email}})
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


# class UserProfileView(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request):
#         serializer = UserProfileSerializer(request.user)
#         return Response(serializer.data)
    
#     def put(self, request):
#         serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer

    # Ensure users only see/update their own profile
    def get_object(self):
        return self.request.user 