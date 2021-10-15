from django import forms
from .models import Todo



#creating a  form

class taskform(forms.ModelForm):

    #class meta creating
    class Meta:

        model = Todo
        
        fields ='__all__'