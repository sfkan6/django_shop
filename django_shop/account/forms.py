from django import forms

from .models import User


class AuthUserForm(forms.Form):
    email = forms.EmailField(max_length=320)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    email.widget.attrs['placeholder'] = 'Email'


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Логин'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Пароль'})
        self.fields['username'].required = True


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'image', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Логин'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['phone'].widget.attrs['placeholder'] = 'Телефон'
