from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
    UserChangeForm,
    UserCreationForm,
)
from django.forms import DateInput, ModelForm

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


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) > 150:
            raise forms.ValidationError('Максимальная длина 150 символов.')
        if not all(char.isalnum() or char in '@/./+/-/_' for char in username):
            raise forms.ValidationError(
                'Можно использовать только буквы, цифры и символы @/./+/-/_.'
            )

        return username


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

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) > 150:
            raise forms.ValidationError('Максимальная длина 150 символов.')
        if not all(char.isalnum() or char in '@/./+/-/_' for char in username):
            raise forms.ValidationError(
                'Можно использовать только буквы, цифры и символы @/./+/-/_.'
            )

        return username
