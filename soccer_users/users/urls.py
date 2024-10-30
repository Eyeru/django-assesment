from django.urls import path
from .views import UserCreateView
from dj_rest_auth.views import LoginView, LogoutView, PasswordResetView

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
]
