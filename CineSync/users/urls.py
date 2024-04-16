from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.urls import reverse_lazy

from users.forms import (
    CustomAuthenticationForm,
    CustomPasswordChangeForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm,
)
from users.views import profile, signup

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        views.LoginView.as_view(
            template_name='users/login.html',
            authentication_form=CustomAuthenticationForm,
        ),
        name='login',
    ),
    path(
        'logout/',
        views.LogoutView.as_view(
            template_name='users/login.html',
        ),
        name='logout',
    ),
    path(
        'password_change/',
        views.PasswordChangeView.as_view(
            template_name='users/password_change.html',
            form_class=CustomPasswordChangeForm,
            success_url=reverse_lazy('users:password_change_done'),
        ),
        name='password_change',
    ),
    path(
        'password_change/done/',
        views.PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html',
        ),
        name='password_change_done',
    ),
    path(
        'password_reset/',
        views.PasswordResetView.as_view(
            template_name='users/password_reset.html',
            email_template_name='users/password_reset_email.html',
            form_class=CustomPasswordResetForm,
            success_url=reverse_lazy('users:password_reset_done'),
        ),
        name='password_reset',
    ),
    path(
        'password_reset/done/',
        views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'password_reset_confirm/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(
            form_class=CustomSetPasswordForm,
            template_name='users/password_reset_confirm.html',
            success_url=reverse_lazy('users:password_reset_confirm_complete'),
        ),
        name='password_reset_confirm',
    ),
    path(
        'password_reset_complete/done/',
        views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
    path('signup/', signup, name='signup'),
    path('profile/', login_required(profile), name='profile'),
]
