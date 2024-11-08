
from django.contrib import admin
from django.urls import path, include
from . import views  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clients.urls')),  # Including clients app URLs
    path('', views.home),  # Root URL for the home view
]
