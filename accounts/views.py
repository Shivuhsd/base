from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from django.core.exceptions import ValidationError
import re
from . utils import send_template_mail
from django.middleware import csrf
from django.conf import settings
import json

# Create your views here.


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            refresh_token = RefreshToken.for_user(user)
            access_token = str(refresh_token.access_token)
            
            response = HttpResponse(
                json.dumps({'access_token': access_token}),
                content_type='application/json',
                status=status.HTTP_200_OK
            )
            
            response.set_cookie(
                key='refresh_token',
                value=str(refresh_token),
                expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                httponly=True,
                secure=True,
                domain='slipwrite.com',
                samesite='Lax',
                path='/'
            )
            
            csrf.get_token(request)
            return response
        
        return Response({'detail': "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
class UserLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.COOKIES.get('refresh_token')

            if not refresh_token:
                return Response(
                    {'detail': 'No refresh token found'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            response = Response({'detail':"Successfully logged out."})

            response.delete_cookie(
                key='refresh_token',
                path='/',
                samesite="Lax",
                domain='localhost:5173',
            )

            return response
        except Exception as e:
            return Response({'detail':'Logout failed'}, status=status.HTTP_400_BAD_REQUEST)
        
        
class UserRegisterView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if email and password are provided
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate email format (basic regex check)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return Response({'error': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if password is strong enough (minimum 8 characters, at least 1 digit)
        if len(password) < 8 or not re.search(r"\d", password) or not re.search(r"[A-Za-z]", password):
            return Response({'error': 'Password must be at least 8 characters long and contain both letters and numbers'},
                             status=status.HTTP_400_BAD_REQUEST)

        # Check if the email is already taken
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email is already registered'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        try:
            User.objects.create_user(username=email, email=email, password=password)
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    

class CustomTokenRefreshView(TokenRefreshView):

    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
      
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return Response({'detail': "Refresh token missing"}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            return Response({'access_token': access_token})
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)



class PasswordResetRequestView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        user = get_object_or_404(User, email = email)
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        
        reset_link = f"https://slipwrite.com/api/accounts/password-reset-confirm/{uid}/{token}/"

        subject = "Password Reset Request"
        body = {'reset_link': reset_link}
        user_email = email

        send_template_mail(user_email, body, 'email/password_reset.html', subject)

        return Response({'message': 'Password reset link sent to email'}, status=status.HTTP_200_OK)
    


class PasswordResetConfirmView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, uid64, token):
        new_password = request.data.get('new_password')
        try:
            uid = force_str(urlsafe_base64_decode(uid64))
            user = User.objects.get(pk = uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'error':'Invalid Link'}, status=status.HTTP_400_BAD_REQUEST)
        
        token_generator = PasswordResetTokenGenerator()
        if token_generator.check_token(user, token):
            user.set_password(new_password)
            user.save()
            return Response({'message':'Password has been reset successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)
