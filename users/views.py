from django.shortcuts import redirect, render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login

from users.email_utils import send_confirmation_email
from users.models import User
from users.serliazers import RegisterSerializer, UserSerializer
from users.utils import check_token


class RegisterView(APIView):
    """Регистрация пользователя"""

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_confirmation_email(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    """Получение списка пользователей"""

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class ConfirmRegistrationView(APIView):
    """Подтверждение регистрации"""

    def get(self, request, uidb64, token):
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


class UserCreateAPIView(generics.CreateAPIView):
    """создание пользователя"""

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SuccessView(APIView):
    """Страница  успешной  регистрации"""

    def get(self, request):
        return render(request, 'users/success.html')


class ErrorView(APIView):
    """Страница  ошибки"""

    def get(self, request):
        return render(request, 'users/error.html')
