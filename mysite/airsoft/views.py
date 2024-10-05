from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# from .models import stuff

# Create your views here.

"""
def login_page(request):
    return HttpResponse("Please, login, sir")
"""
def login_page(request):
    return render(request, "airsoft/login.html")
