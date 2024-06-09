from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserView, ConfirmCodeView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm_code', ConfirmCodeView.as_view(), name='confirm_code'),
    path('user/', UserView.as_view(), name='user'),
    path('user/create/', UserCreateAPIView.as_view(), name='user_create'),
]
