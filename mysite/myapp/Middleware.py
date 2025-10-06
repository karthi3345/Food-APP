# users/middleware.py

from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse

class LoginRequestViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.public_paths = [
            reverse('users:login'),    # Fixed namespace here
            reverse('users:register'), # Assuming you have a signup/register view named 'register'
            '/admin/',                 # Admin path stays as is
        ]

    def __call__(self, request):
        path = request.path

        # Allow access to public paths
        if any(path.startswith(p) for p in self.public_paths):
            return self.get_response(request)

        # Allow authenticated users
        if request.user.is_authenticated:
            return self.get_response(request)

        # Redirect unauthenticated users to login
        return redirect(settings.LOGIN_URL)
