from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .utils import get_client_ip, get_ip_location, get_current_datetime
from django.contrib.auth.decorators import login_required


# Register View
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            ip = get_client_ip(request)
            location_data = get_ip_location(ip)
            current_time = get_current_datetime()

            messages.success(
                request,
                f"Welcome {user.username}! IP: {ip}, City: {location_data.get('city')}, "
                f"Country: {location_data.get('country')}, Registered at: {current_time}"
            )
            return redirect("myapp:index")  # redirect after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, "users/register.html", {"form": form})


# Login View
def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect("myapp:index")  # redirect after successful login
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = CustomAuthenticationForm()

    return render(request, "users/login.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return render(request, "users/logout.html")

def profile(request):
    return render(request,"users/profile.html")