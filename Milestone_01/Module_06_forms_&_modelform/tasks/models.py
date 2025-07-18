from django.db import models

# Create your models here.

# let's create table

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name
    


class Task(models.Model):
    # Many to one at child
    project = models.ForeignKey(
        "Project", 
        on_delete=models.CASCADE, 
        # null=True,   #one kind of solution for non-nullable field
        # blank=True
        
    # second approach
        default=1 #default=1 Project id 1
    )
    
    # many to many
    assigned_to = models.ManyToManyField(Employee)
    
    
    
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # taskdetails auto create column while create one to one connection: modelName
    
    
# convert this into postgresql: query using this command
# python manage.py makemigrations
# python manage.py migrate


# Relationship
    # One to one
    # Many to one
    # Many to many


# one to one
class TaskDetail(models.Model): # dependent to Task
    # best practice
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    # constant in CAPITAL form
    PRIORITY_OPTIONS = (
        (HIGH,'High'),
        (MEDIUM,'Medium'),
        (LOW,'Low')
        
    )
    # Relation
    task = models.OneToOneField(Task, on_delete = models.CASCADE)
    
    
    
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1,choices=PRIORITY_OPTIONS, default='L')
    
    
    
    
# -------------------------------------------------------------------------------
# to insert data using shell
# -------------------------------------------------------------------------------
# python manage.py shell
# from tasks.models import Task
# t = Task(title="low priority tasks", description="dsfdf",due_date="2024-12-12")
# t.save()


# get query
# task = Task.objects.get(id=1) 
# means:
    # select * from task where id = 2
# this tecnique called as ORM = Object-Relational Mapper




# Many to one Relationship

class Project(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    
    


# Many to Many Relationship

# task = onekgula employee ekta task
# employee = onekgula task er jonno assign ase