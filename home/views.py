from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Contact
from .forms import ContactForm
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    
    context = {

    }

    return render(request, 'home/index.html', context)


def about(request):

    context = {

    }
    
    return render(request, 'home/about.html', context)

def contact(request):

    contacts = Contact.objects.all()
    
    for i in contacts:
        print(i.name)
    
    
    
    context = {

    }
    
    return render(request, 'home/contact.html', context)

def case_studies(request):

    context = {

    }

    return render(request, 'home/case-studies.html', context)


#Ajax form submission
def ajax_contact(request):

    data = dict()

    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            data['form_is_valid'] = True
            
            data['success_form'] = render_to_string('home/forms/contact_form_success.html', request=request)
            
        
        else:
            data['form_is_valid'] = False
    
    else:
        form = ContactForm()
    
    
    return JsonResponse(data)

