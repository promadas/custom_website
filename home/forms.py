from django import forms
from .models import Contact

# Create the form class.
class ContactForm(forms.ModelForm):
    
    # Specify the name of model to use
    class Meta:
        
        model = Contact
        fields = '__all__'