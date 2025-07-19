from django.urls import path
from tasks.views import manager_dashboard,user_dashboard,test,create_task,create_Model_task

urlpatterns = [
    path("manager-dashboard/",manager_dashboard),
    path("user-dashboard/",user_dashboard),
    path("test/",test),
    # module-6
    path("create-task/",create_task),
    path("create-model-task/",create_Model_task)
]
