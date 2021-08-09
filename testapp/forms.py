from django import forms
from testapp.models import User
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'please enter password'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        try:
            user = User.objects.get(email)
            if not(user and user.check_password(password)):
                raise ValidationError('Invalid Email & Password combination')
        except User.DoesNotExist:
            raise ValidationError('Invalid Email')