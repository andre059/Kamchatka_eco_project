from django.urls import path


from users.apps import UsersConfig
from users.views import RegisterView, UserView, ConfirmRegistrationView, UserCreateAPIView, SuccessView, ErrorView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm_registration/<str:uidb64>/<str:token>/', ConfirmRegistrationView.as_view(), name='confirm_registration'),
    path('user/', UserView.as_view(), name='user'),
    path('user/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('success/', SuccessView.as_view(), name='your_success_page'),
    path('error/', ErrorView.as_view(), name='your_error_page'),
]
