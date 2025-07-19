# module-6
from django import forms
# from tasks.models import Task

class TaskForm(forms.Form): #inherit built-in Form
    title = forms.CharField(max_length=250) #charfield(optional)
    
    description = forms.CharField(
        label="Task Description",
        widget=forms.Textarea(
            attrs={
                'placeholder':'Enter task descripition here'
            }
        )
    )
    
    due_date = forms.DateField(
        label="Due Date:",
        widget=forms.SelectDateWidget
    )
    
    assigned_to = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[],
        label="Assigned To"
    )
    
    # fetching employee data
    def __init__(self,*args, **kwargs):
        # print(args, kwargs)
        # before pop output : () {}
        # after pop output: () {'employees': {'name': 'John', 'id': 1}}

        # remove employee form kargs before we pass it into **kwargs
        employees = kwargs.pop("employees",[]) # "employees" form view.py
        # print("Pop korar pore: ",args, kwargs)
        # output: () {}
        print(employees)        
        
        # similar to implement initializable
        # super().__init__(args, kwargs) # 'tuple' object has no attribute 'get'
        # fix:
        super().__init__(*args,**kwargs) # * use to unpack * tuple or ** dictionary 
        # print(self.fields)
        self.fields['assigned_to'].choices = [
            (emp.id, emp.name) for emp in employees #using list comprehension
        ]
        





# Django model form: used to minimize  the redundancy of previous form with similar field at view.py and forms.py
from tasks.models import Task

class TaskModelForm(forms.ModelForm):
    class Meta: # it controlls the behaviour of TaskModelForm class
        model = Task
        # fields = '__all__' #when we want to use all field
        
        # what if you want specific field
        fields = ['title','description','due_date','assigned_to']
        # when we exclude some fields
        # exclude = ['project','is_completed','created_at', 'updated_at']
        
        # widgets work on Meta class
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'class' : "border-2 border-gray-300 w-full rounded-lg shadow-sm focus:border-rose-500 focus:ring-rose-500"
                }    
            ),
            'due_date' : forms.SelectDateWidget,
            'assigned_to' : forms.CheckboxSelectMultiple
        }