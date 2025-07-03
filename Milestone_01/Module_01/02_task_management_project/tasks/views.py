# main work: writing logical funciton 


from django.shortcuts import render

# importing http response
from django.http import HttpResponse

# Create your views here.
def home(request):
    # Wrok with database
    # Transform data
    # data pass
    # HTTP response / Json Response

    return HttpResponse("Welcome to the task management system")

# to call this function we need to configure urls at task_management package


def contact(request):
    return HttpResponse("<h1 style='color: purple'>This is contact page</h1>")


def show_task(request):
    return HttpResponse("This is our task page")