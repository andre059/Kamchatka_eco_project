from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.shortcuts import redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login

from users.email_utils import send_confirmation_email
from users.models import User
from users.serliazers import RegisterSerializer, UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_confirmation_email(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def check_token(user, token):
    """Проверка токена для подтверждения регистрации"""

    return PasswordResetTokenGenerator().check_token(user, token)


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def confirm_registration(request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('your_success_page')  # Перенаправление на страницу успешной регистрации
        else:
            return redirect('your_error_page')  # Перенаправление на страницу ошибки
