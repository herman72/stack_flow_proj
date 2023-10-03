from django import forms
from django.core.exceptions import ValidationError

from .models import User


class UserUpdateForm(forms.ModelForm):
    pass


class UserRegisterForm(UserUpdateForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'phone_number', 'national_id']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already exist!")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already exist!")
        return username

class UserLoginForm(forms.Form):
    pass