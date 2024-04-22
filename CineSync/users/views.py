from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.translation import gettext as _

from users.forms import ProfileForm, SignUpForm, UserForm
from users.models import Profile

__all__ = []


def signup(request):
    form = SignUpForm(request.POST)
    template = 'users/signup.html'
    context = {
        'form': form,
        'text_button': 'Зарегистрироваться',
    }
    if request.method == 'GET':
        return render(request, template, context)

    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        Profile.objects.create(user=user)
        user.profile.save()
        messages.success(request, _('Пользователь упешно создан'))
        return redirect(reverse('users:login'))

    return render(request, template, context)


def profile(request):
    profile_form = ProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=request.user.profile,
    )
    user_form = UserForm(
        request.POST or None,
        instance=request.user,
    )

    if request.method == 'POST':
        if all((profile_form.is_valid(), user_form.is_valid())):
            profile_form.save()
            user_form.save()
            return redirect(reverse('users:profile'))

    return render(
        request,
        'users/profile.html',
        {
            'profile_form': profile_form,
            'user_form': user_form,
            'user': request.user,
        },
    )
