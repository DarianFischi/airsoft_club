from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import is_valid_path
from urllib.parse import urlparse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.http import JsonResponse

def login_view(request):
    next_url = request.GET.get('next', '/')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Ensure next_url is safe or default to home page
            next_url = request.POST.get('next', next_url)
            parsed_url = urlparse(next_url)
            if not parsed_url.netloc and is_valid_path(next_url):
                return HttpResponseRedirect('/events/')
            return HttpResponseRedirect('/login/')
    else:
        form = AuthenticationForm()

    return render(request, 'authz/login.html', {'form': form, 'next': next_url})


def home(request):
    return render(request, 'authz/home.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        
        if (password != password2):
            messages.info(request, "Passwords Don't Match")
        else:
            try:
                password_validation.validate_password(password)
            
                user = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    username = username
                )

                user.set_password(password)
                user.save()

                messages.info(request, "Account created Successfully!")
            except ValidationError as e:
                return JsonResponse({'errors': e.messages}, status=400)

        return redirect('/register/')

    return render(request, 'authz/register.html')


@login_required
def secure_view(request):
    return render(request, 'authz/secure.html')


def logout_view(request):
    logout(request)
    return redirect('/')


