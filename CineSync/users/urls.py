from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.urls import reverse_lazy

from users.forms import (
    CustomAuthenticationForm,
    CustomPasswordChangeForm,
)
from users.views import profile, signup

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        views.LoginView.as_view(
            template_name='users/login.html',
            authentication_form=CustomAuthenticationForm,
            extra_context={
                'text_button': 'Войти',
            },
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
    path('signup/', signup, name='signup'),
    path('profile/', login_required(profile), name='profile'),
]
