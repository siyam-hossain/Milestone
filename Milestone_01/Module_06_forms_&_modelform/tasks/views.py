from django.shortcuts import render
from django.http import HttpResponse

# module-6
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee,Task

def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")


def user_dashboard(request):
    # dashboard is a folder at templates
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    # module 4.5: context in Django
    context = {
        "names": ["Mahmud", "Siyam","Hossain"],
        "age": 20,
    }
    return render(request,"test.html",context)



# module-6
# def create_task(request):
#     employees = Employee.objects.all()
#     form = TaskForm(employees = employees) #by default for GET
    
#     if request.method == "POST":
#         form = TaskForm(request.POST,employees = employees)
#         # print(form)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             data = form.cleaned_data
#             title = data.get('title')
#             description = data.get('description')
#             due_date = data.get('due_date')
#             assigned_to = data.get('assigned_to')
            
#             task = Task.objects.create(title = title, description=description, due_date = due_date)
            
#             # assign employee to tasks
#             for emp_id in assigned_to:
#                 emp = Employee.objects.get(id = emp_id)
#                 task.assign_to.add(emp)
            
#             return HttpResponse("Task Added Successfully")
        
#     context = {"form":form}
#     return render(request, "task_form.html", context)



# for model form

def create_task(request):
    employees = Employee.objects.all()
    form = TaskModelForm() 
    
    
    if request.method == "POST":
        form = TaskModelForm(request.POST)

        if form.is_valid():
            print(form)
            form.save()
            
            
            return HttpResponse("Task Added Successfully")
        
    context = {"form":form}
    return render(request, "task_form.html", context)