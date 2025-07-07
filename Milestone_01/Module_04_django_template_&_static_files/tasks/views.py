from django.shortcuts import render

from django.http import HttpResponse

'''
def home(request):
    # render(request, "templates") : it knows the directory of templates because of settings.py TEMPLATES = []
    # return render(request,"home.html")
    return HttpResponse("Home")
'''

def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")


def user_dashboard(request):
    # dashboard is a folder at templates
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    return render(request,"test.html")