from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # Work with database
    # Perform CRUD operations
    # Create a new record
    # Read records
    # Update records
    # Delete records
    # Perform any other operations you need
    return HttpResponse("Welcome to the task management system!")

def contact(request):
    return HttpResponse("<h1 style = 'color: red'>Contact us at: sharif@uni-bremen.de</h1>")

def show_task(request):
    return HttpResponse("<h1 style = 'color: blue'>Task: Complete the Django project</h1>")



