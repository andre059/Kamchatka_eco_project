from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserView.as_view(), name='user'),
]
