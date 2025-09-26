# myapp/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class LoginRequestViewMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response  # Corrected: get_response, not get-response

    def __call__(self, request):
        # List of public paths that can be accessed without login
        public_paths = [
            reverse('login'),  # Add your login URL name
            reverse('signup'),  # Add your signup URL name
            reverse('admin:login'),  # Django admin login
            '/static/',  # Static files path
        ]

        # If the user is not authenticated and they're trying to access a restricted page
        if not request.user.is_authenticated:
            path = request.path
            if not any(path.startswith(p) for p in public_paths):
                return redirect('login')  # Redirect to login page (you may change 'login' to your path name)

        # If the user is authenticated, or if they are visiting a public page, continue
        response = self.get_response(request)
        return response
