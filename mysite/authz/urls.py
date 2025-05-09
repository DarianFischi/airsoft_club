from django.urls import path
from .views import home, login_view, secure_view, logout_view, register_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('secure/', secure_view, name='secure_view'),
    path('logout/', logout_view, name='logout'),
]
