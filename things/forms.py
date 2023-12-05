"""Forms of the project."""
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm): 
    """Form enabling unregistered users to create tasks for a team."""
     
    class Meta: 
        model = Thing
        fields = ['name', 'description', 'quantity'] 
        widgets = {'description':forms.Textarea(), 'quantity':forms.NumberInput()}
