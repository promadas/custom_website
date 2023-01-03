from django import forms
from .models import Contact, JobsApply

# Create the form class.
class ContactForm(forms.ModelForm):
    
    # Specify the name of model to use
    class Meta:
        
        model = Contact
        fields = '__all__'

class JobsApplyForm(forms.ModelForm):
    
    class Meta:
        
        model = JobsApply
        fields = '__all__'