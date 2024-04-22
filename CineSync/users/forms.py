from django import forms
from django.contrib.auth import get_user_model
from django.forms import DateInput, ModelForm
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    UserChangeForm,
    UserCreationForm,
)

from users.models import Profile

__all__ = []


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta(forms.ModelForm):
        model = Profile


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta(forms.ModelForm):
        fields = ('old_password', 'new_password', 'approve_new_password')


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta(forms.ModelForm):
        fields = ('old_password', 'new_password', 'approve_new_password')


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta(forms.ModelForm):
        fields = ('old_password', 'new_password', 'approve_new_password')


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta(ModelForm):
        model = Profile
        fields = [
            model.birthday.field.name,
            model.image.field.name,
        ]
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = [
            model.username.field.name,
            model.first_name.field.name,
            model.last_name.field.name,
        ]


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta(forms.ModelForm):
        model = get_user_model()
        fields = [
            model.username.field.name,
            model.first_name.field.name,
            model.last_name.field.name,
        ]
