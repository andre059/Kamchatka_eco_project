from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserView, ConfirmCodeView, UserUpdateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm_code', ConfirmCodeView.as_view(), name='confirm_code'),
    path('user/', UserView.as_view(), name='user'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update')
]
