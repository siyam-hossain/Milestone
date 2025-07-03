"""
URL configuration for task_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

# importing utility form tasks:package - like class, function etc
from tasks.views import home,contact

# now attach include()
from django.urls import include



# inside urlpatterns every method consider as element
urlpatterns = [
    path('admin/', admin.site.urls),

    # urlpatterns help us to call any function form view
    # path use while mapping url
    # parth("route/","view")
    # path("home/", home)
    
    
    # if we consider it as homepage then route must be empty
    path("",home),
    
    # lets add contact view
    path("contact/",contact),
    
    # now we include all urls at tasks app or package
    # include("app or package name .urls") to let it know there are some others urls as well
    path("tasks/", include("tasks.urls"))
]
