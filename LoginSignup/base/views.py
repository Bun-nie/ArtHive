from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm, CustomPasswordChangeForm
from django.contrib import messages
from shop.models import Order
from django.contrib.auth import update_session_auth_hash

# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()
# for login
# cleaned code from the previous 
@login_required
def home(request):
    return render(request, "homepage/gallery.html", {})

def landing(request):
    return render(request, "landing.html", {})

def aboutUs(request):
    return render(request, "about.html", {})

@login_required
def profile_settings(request):
    return render(request, "profile-settings.html", {})

@login_required
def userProfile(request):
    if request.user.is_staff:
        return render(request, "admin-profile.html", {})
    else:
        return render(request, "home.html", {})

@login_required
def viewHoneycomb(request):
    return render(request, 'honeycomb/honey-comb-main.html', {})

@login_required
def viewOrderTrack(request):
    user = request.user
    pk = request.user.id
    order = Order.objects.get(id = pk)

    context = {
        'order': order,
        'order_items': order.orderitem_set.all(),
        'total_price': order.get_cart_total,
        'total_items': order.get_cart_items(),
    }

    return render(request, 'honeycomb/order-track.html', context)



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

def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            # Save the new password
            form.save()
            # Update session to keep user logged in after password change
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password was successfully updated!")
            return redirect('landing')  # Redirect to a success page
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})


