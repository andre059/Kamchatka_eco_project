from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.utils import send_confirmation_email
from users.models import User
from users.serliazers import RegisterSerializer, UserSerializer


class RegisterView(APIView):
    """Регистрация пользователя"""

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_confirmation_email(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmCodeView(APIView):
    """Подтверждение регистрации"""

    def post(self, request):
        try:
            user = User.objects.get(email=request.data.get('email'))
        except User.DoesNotExist:
            return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)
        if user.confirmation_code == int(request.data.get('code')):
            user.is_active = True
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Неверный код'}, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    """Получение списка пользователей"""

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserUpdateAPIView(APIView):
    """Изменение данных пользователя по ID"""

    def put(self, request, pk):
        # Получаем пользователя по ID
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

        # Сохраняем изменения
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
