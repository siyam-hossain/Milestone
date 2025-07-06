from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path


from tasks.views import home,contact
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),

    path("",home),

    path("contact/",contact),
    
    path("tasks/", include("tasks.urls"))
]