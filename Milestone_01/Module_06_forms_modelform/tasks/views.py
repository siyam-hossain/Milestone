from django.shortcuts import render
from django.http import HttpResponse

# module-6
from tasks.forms import TaskForm
# 
from tasks.models import Employee,Task,Project

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


# for form
def create_task(request):
    # fetch data form database insted of shell command
    employees = Employee.objects.all()
    
    
    # create a form
    # form = TaskForm()
    
    # forwording form with dictionary : static way
    # form = TaskForm(
    #     employees = {
    #         "name":"John",
    #         "id": 1
    #     } 
    # )
    
    
    # forwording form with dictionary : dynamic way
    form = TaskForm(
        employees = employees
    ) # for GET
    
    # working with post request: 6.3 M
    if request.method == "POST":
        form = TaskForm(
            request.POST,
            employees = employees
        )
        # print(form) # unclean data  
        if form.is_valid():
            # print(form.cleaned_data) # clean data
            # let's create entry data and extract data from form
            data = form.cleaned_data
            # print(data)

            
            title = data.get('title')
            description = data.get('description')
            due_date = data.get('due_date')
            assigned_to = data.get('assigned_to')
            
            task = Task.objects.create(
                title = title, 
                description = description, 
                due_date = due_date
            )
            
            # Assign employee to tasks
            for emp_id in assigned_to:
                employee = Employee.objects.get(id = emp_id) 
                task.assigned_to.add(employee)
            
            # confirmation
            return HttpResponse("Task Added sccessfull")
    
    
    
    # context work as a dictionary
    context = {"form": form}
    return render(
        request, 
        "task_form.html",
        context
    )



# for Model Form
# import here
from tasks.forms import TaskModelForm

def create_Model_task(request):

    # employees = Employee.objects.all()
    
    form = TaskModelForm()
    
    if request.method == "POST":
        form = TaskModelForm(
            request.POST
        )

        if form.is_valid():
            form.save()
            
            # confirmation message at same page
            return render(
                request,
                'task_form.html',
                {
                    "form":form,
                    "message":"task added successfully :)"
                }
            )
            
    
    context = {"form": form}
    return render(
        request, 
        "task_form.html",
        context
    )













