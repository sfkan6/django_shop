from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.edit import UpdateView
from django.contrib import messages

from .forms import UserRegistrationForm, AuthUserForm, UserUpdateForm
from .models import User
from .services import auth_user, signup_user 
# Create your views here.


def auth(request):
    data = {}
    if request.method == 'POST':
        form = AuthUserForm(request.POST or None)
        if auth_user(request, form):
            return redirect('home')

        data['form'] = form
        messages.error(request, 'Неправильно введены данные')
        return render(request, 'login.html', data)

    else:
        data['form'] = AuthUserForm
        return render(request, 'login.html', data)


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if signup_user(form):
            return redirect('auth')
    else:
        form = UserRegistrationForm
        return render(request, 'signup.html', {'form': form})


class Profile(UpdateView):
    model = User
    template_name = 'profile.html'
    success_url = '/auth/{id}'
    form_class = UserUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')
