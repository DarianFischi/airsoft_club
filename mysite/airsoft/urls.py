from django.urls import path

from . import views


app_name = "airsoft"  #namespacing to help browser find url of THIS app
urlpatterns = [
    path('login_page', views.login_page, name="login_page")      
]
