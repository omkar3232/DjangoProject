
# Register your models here.
from django.contrib import admin
from .models import Client, Project


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'created_at', 'created_by')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'client', 'created_at', 'created_by')
    filter_horizontal = ('users',)  # Allows selection of users in a filter box
