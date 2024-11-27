from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.

# for login
# cleaned code from the previous 
@login_required
def home(request):
    return render(request, "homepage/gallery.html", {})

def landing(request):
    return render(request, "landing.html", {})

def aboutUs(request):
    return render(request, "about.html", {})

# for authorization
def authView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                # username already exists
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already taken. Please choose another one.')
                else:
                    # create user if username is not taken
                    user = User.objects.create_user(
                        username = username,
                        email = email,
                        first_name = firstname,
                        last_name = lastname,
                        password = password # will not be hashed
                    )
                    user.save()

                # if registration is a success. 
                # redirects to login page
                messages.success(request, 'Profile registered successfully! You can now log in')
                return redirect("login")
            else:
                messages.error(request, 'Passwords do not match!')
    else:
        form = SignUpForm()
    
    return render(request, "registration/signup.html", {"form": form})

