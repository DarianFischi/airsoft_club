"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from events import views
# media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("airsoft/", include("airsoft.urls")),
    path('admin/', admin.site.urls),
    path('', include("authz.urls")),
    # for reverse lookup using login and logout
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('', include('django.contrib.auth.urls'))
    
    # Consider a re_path here
    path('events/', include('events.urls')), 
    path('calendar/events/', views.get_events, name='get_events'),
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
