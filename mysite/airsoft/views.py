from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# from .models import stuff

# Create your views here.

"""
def login_page(request):
    return HttpResponse("Please, login, sir")
"""
def main_page(request):
    return HttpResponse("Well done, you have made it to the main page.")

## Look into if this one does anything