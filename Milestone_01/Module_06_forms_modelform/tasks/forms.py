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
        








class StyledFormMixin:
    '''Mixing to apply style to form field'''
    
    default_classes = "border-2 border-gray-500 w-full p-3 rounded-lg shadow-xl focus:outline-none focus:border-rose-500 focus:ring-rose-500"
    
    def apply_styled_widgets(self):
        # mixing by default work as dictionary
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update(
                    {
                        'class':self.default_classes,
                        'placeholder': f"Enter{field.label.lower()}"
                    }
                )
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update(
                    {
                        'style':"resize:none",
                        'class':self.default_classes,
                        'placeholder': f"Enter{field.label.lower()}"
                        
                    }
                )
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update(
                    {
                        'class':"border-2 border-gray-500 p-3 rounded-lg shadow-xl focus:outline-none focus:border-rose-500 focus:ring-rose-500"
                    }
                )
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update(
                    {
                        'class': "space-y-2"
                    }
                )
            else:
                print("inside else")
                field.widget.attrs.update(
                    {
                        'class':self.default_classes
                    }
                )
        





# organised and reduce redundency 
from tasks.models import Task
# always mixing first then others
class TaskModelForm(StyledFormMixin,forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','due_date','assigned_to']
        widgets = {
            'due_date' : forms.SelectDateWidget,
            'assigned_to': forms.CheckboxSelectMultiple
        }
    
    
    '''using Mixing widget (not in meta class)'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
    










# unorganised 
'''
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
        
        
        # manual widget
        # widgets work on Meta class
        widgets = {
            'title' : forms.TextInput(
                attrs={
                   'class': "w-full p-2 border-2 border-gray-500 rounded-lg shadow-sm",
                    'placeholder': "Enter task title"
                }    
            ),
            'description':forms.Textarea(
                attrs={
                    'style':"height:150px; border-color:gray",
                    'class' : "w-full p-2  border-2 border-rose-500 rounded-lg shadow-sm",
                    'placeholder':"Describe the task"
                } 
            ),
            'due_date' : forms.SelectDateWidget(
                attrs={
                    'class' : "border-2 border-gray-500 rounded-lg shadow-sm mb-1"
                }     
            ),
            'assigned_to' : forms.CheckboxSelectMultiple(
                attrs={
                    'class' : "w-full border-2 border-gray-300 rounded-lg shadow-sm flex flex-row items-center gap-4",
                } 
            )
        }
'''