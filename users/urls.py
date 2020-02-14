from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    #Login Logout URLS
    #   By default views looks login template inside template/registration/ folder
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    
    #Password Reset Buil-in functionality --- Required email backend server running
    path('password-reset/', views.PswResetView.as_view(), name='password_reset'),    

                                # Paramters required for confirmation of user || uidb64 - user ID in 64 bits
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/request/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_request.html'), name='password_reset_done'),
    path('password-reset/confirm/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
