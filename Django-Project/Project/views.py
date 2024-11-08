from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Django Machine Test ,API project! Access the API at /api/")
