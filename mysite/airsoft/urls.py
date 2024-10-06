from django.urls import path

from . import views


app_name = "airsoft"  #namespacing to help browser find url of THIS app
urlpatterns = [
    path('', views.main_page, name="main_page")      
]
