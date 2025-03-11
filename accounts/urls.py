from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='token_obtain'),
  
    path('token/refresh/', views.CustomTokenRefreshView.as_view(), name='token_refresh'),

    path('user-register/', views.UserRegisterView.as_view(), name='user-register'),

    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    # Password reset views

    path('reset-password/', views.PasswordResetRequestView.as_view(), name='password_reset_view'),
    path('password-reset-confirm/<str:uid64>/<str:token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

