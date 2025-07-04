from django.urls import path 
from tasks.views import show_task, show_specific_task
# or
# from .views import show_task


# we use this approach inorder to connect own package views function or methods


# remember django always look url at actual project package urls.py rather than other newly created apps or package what ever you say
urlpatterns = [
    path('show-task/',show_task),
    
    
    # for dynamic urls <dynamic>
    path("show-task/<int:id>", show_specific_task)
    
]



