from django.contrib.auth.models import User
from django import forms
from django_recaptcha.fields import ReCaptchaField
from django.contrib.auth.forms import UserCreationForm

class RecoverForm(forms.Form):
    email = forms.EmailField()
    
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={
        'placeholder': 'password'
    }))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={
        'placeholder': 'again password'
    }))


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    captcha_field=ReCaptchaField()