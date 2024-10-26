from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Client, Project
from .forms import ClientForm, ProjectForm
import json

# Client Views
@csrf_exempt
def client_list(request):
    if request.method == 'GET':
        clients = Client.objects.all().values('id', 'client_name', 'created_at', 'created_by__username')
        return JsonResponse(list(clients), safe=False)

@csrf_exempt
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'GET':
        client_data = {
            'id': client.id,
            'client_name': client.client_name,
            'created_at': client.created_at,
            'created_by': client.created_by.username,
            'projects': list(client.projects.values('id', 'project_name')),
        }
        return JsonResponse(client_data)
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        form = ClientForm(data, instance=client)
        if form.is_valid():
            updated_client = form.save()
            return JsonResponse({'message': 'Client updated successfully', 'client': {'id': updated_client.id, 'client_name': updated_client.client_name}})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    elif request.method == 'DELETE':
        client.delete()
        return JsonResponse({'message': 'Client deleted successfully'}, status=204)

@csrf_exempt
def client_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        form = ClientForm(data)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            client.save()
            return JsonResponse({'message': 'Client created successfully', 'client': {'id': client.id, 'client_name': client.client_name}}, status=201)
        else:
            return JsonResponse({'error': form.errors}, status=400)

# Project Views
@csrf_exempt
def project_list(request):
    if request.method == 'GET':
        projects = Project.objects.all().values('id', 'project_name', 'client__client_name', 'created_at', 'created_by__username')
        return JsonResponse(list(projects), safe=False)

@csrf_exempt
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'GET':
        project_data = {
            'id': project.id,
            'project_name': project.project_name,
            'client': project.client.client_name,
            'created_at': project.created_at,
            'created_by': project.created_by.username,
            'users': list(project.users.values('id', 'username')),
        }
        return JsonResponse(project_data)
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        form = ProjectForm(data, instance=project)
        if form.is_valid():
            updated_project = form.save()
            updated_project.users.set(data.get('users', []))
            return JsonResponse({'message': 'Project updated successfully', 'project': {'id': updated_project.id, 'project_name': updated_project.project_name}})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    elif request.method == 'DELETE':
        project.delete()
        return JsonResponse({'message': 'Project deleted successfully'}, status=204)

@csrf_exempt
def project_create(request, client_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        client = get_object_or_404(Client, pk=client_id)
        form = ProjectForm(data)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = client
            project.created_by = request.user
            project.save()
            project.users.set(data.get('users', []))
            return JsonResponse({'message': 'Project created successfully', 'project': {'id': project.id, 'project_name': project.project_name}}, status=201)
        else:
            return JsonResponse({'error': form.errors}, status=400)
