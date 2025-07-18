# module-6
from django import forms
from tasks.models import Task


# Django Form

class TaskForm(forms.Form):
    title = forms.CharField(max_length=250, label="Task Title")
    description = forms.CharField(widget=forms.Textarea,label="task description")
    due_date = forms.DateField(widget=forms.SelectDateWidget,label="Due Date: ")
    
    assigned_to = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        # default choices
        choices=[], label="Assigned To: "
        )
    
    # extracting or fetching data from database
    def __init__(self,*args, **kwargs):
        # print(args,kwargs)
        
        employees = kwargs.pop("employees",[]) #remove employees from kwargs  
        # print("pop korar pore",args,kwargs)
        print(employees)
        
        super().__init__(*args, **kwargs) #concept: unpack (python)
        
        print(self.fields)
        self.fields['assigned_to'].choices = [(emp.id,emp.name) for emp in employees]
        
    

# Django Model Form
class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = '__all__' # when you want to get all fields
        fields = ['title','description','due_date','assigned_to'] #this thing we take
        # exclude = ['project', 'is_completed', 'created_at', 'updated_at']