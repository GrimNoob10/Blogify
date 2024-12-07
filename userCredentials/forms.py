from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove default help texts
        self.fields['username'].help_text = None
        self.fields['email'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        
        # # Optionally change labels
        # self.fields['username'].label = "Username"
        # self.fields['email'].label = "Email Address"
        # self.fields['password1'].label = "Password"
        # self.fields['password2'].label = "Confirm Password"
        

from django.utils.translation import gettext_lazy as _

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].label = _("Username or Email")
        self.fields['password'].label = _("Password")

        # Optionally, remove help texts
        self.fields['username'].help_text = None
        self.fields['password'].help_text = None
        

