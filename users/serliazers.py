from django.contrib.auth.hashers import check_password
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя"""

    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            password1 = validated_data.pop('password')
            password2 = validated_data.pop('password2')

            if password1 != password2:
                raise serializers.ValidationError("Пароли не совпадают.")

            user = User.objects.create(validated_data)
            user.set_password(password1)
            user.save()
            return user


class ChangePasswordSerializer(serializers.Serializer):
    """Сериализатор для изменения пароля"""

    old_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not check_password(value, user.password):
            raise serializers.ValidationError('Ваш старый пароль введен неправильно. Пожалуйста, введите его снова.')
        return value

    def validate(self, data):
        if not all(data.values()):
            raise serializers.ValidationError("Заполните все обязательные поля.")

        new_password1 = data.get('new_password1')
        new_password2 = data.get('new_password2')

        if new_password1 != new_password2:
            raise serializers.ValidationError("Новые пароли не совпадают.")

        return data