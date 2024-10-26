from django.urls import path
from .views import (
    client_list,
    client_detail,
    client_create,
    project_list,
    project_detail,
    project_create,
)

urlpatterns = [
    path('clients/', client_list, name='client_list'),
    path('clients/<int:pk>/', client_detail, name='client_detail'),
    path('clients/create/', client_create, name='client_create'),
    path('clients/<int:client_id>/projects/create/', project_create, name='project_create'),
    path('projects/', project_list, name='project_list'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
]
