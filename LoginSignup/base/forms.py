from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email", max_length=50)
    firstname = forms.CharField(label="First Name", max_length=100)
    lastname = forms.CharField(label="Last Name", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['old_password', 'new_password1', 'new_password2']
        widgets = {
            'old_password': forms.Textarea(
                attrs={
                    'class': 'input-field',
                    'placeholder': 'Old password',
                    'rows': 1
                }
            ),
            'new_password1': forms.Textarea(
                attrs={
                    'class': 'input-field',
                    'placeholder': 'New Password',
                    'rows': 1
                }
            ),
            'new_password2': forms.Textarea(
                attrs={
                    'class': 'input-field',
                    'placeholder': 'Confirm New Password',
                    'rows': 1
                }
            ),
        }