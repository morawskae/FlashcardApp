from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView 

from ..serializers import RegisterSerializer

User = get_user_model()

class RegisterApiView(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if(serializer.is_valid()):
            user = serializer.save()
            token, created  = Token.objects.get_or_create(user=user)
            return Response({
                "user":{
                    "id": user.id,
                    "username":user.username,
                    "email":user.email,
                },
                "token": token.key,
                }, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class LoginApiView(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response({
                "detail":"Username and password are required"
            }, status= status.HTTP_400_BAD_REQUEST)
        user = authenticate(request=request, username=username, password=password)
        if user is None:
             return Response({
                "detail":"Username or password is invalid"
            }, status= status.HTTP_401_UNAUTHORIZED)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
                "user":{
                    "id": user.id,
                    "username":user.username,
                    "email":user.email,
                },
                "token": token.key,
                }, status = status.HTTP_200_OK)

class LogoutApiView(APIView):
    permission_classes= [IsAuthenticated]

    def post(self,request):
        if request.auth is not None:
            request.auth.delete()
        return Response(
            {
                "detail":"Successfully logged out"
            },
            status = status.HTTP_200_OK
        )