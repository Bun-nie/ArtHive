from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email", max_length=50)
    firstname = forms.CharField(label="First Name", max_length=100)
    lastname = forms.CharField(label="Last Name", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")