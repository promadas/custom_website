from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Contact, JobsApply
from .forms import ContactForm, JobsApplyForm
from django.template.loader import render_to_string

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def dashboard(request):

    applies = JobsApply.objects.all()
    
    
    context = {
        'applies': applies

    }

    return render(request, 'dashboard/index.html', context)



@login_required
def jobs_apply_delete(request, pk):
        
    apply = JobsApply.objects.get(id=pk)
    
    if request.method == 'POST':

        apply.delete()
        messages.success(request, 'Apply deleted successfully!')
        return redirect('/dashboard/')
    
    else:
        redirect(request.path_info)

    context = {
        'apply': apply,
    }

    return render(request, 'dashboard/delete.html', context)


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


def career(request):

    context = {

    }

    return render(request, 'home/career.html', context)


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


# Services views
def medical_solution(request):

    context = {

    }

    return render(request, 'home/services/medical-solution.html', context)

def mobile_app(request):

    context = {

    }

    return render(request, 'home/services/mobile-app.html', context)

def erp_solution(request):

    context = {

    }

    return render(request, 'home/services/erp-solution.html', context)

def e_commerce_solution(request):

    context = {

    }

    return render(request, 'home/services/e-commerce.html', context)

def cyber_security(request):

    context = {

    }

    return render(request, 'home/services/cyber-security.html', context)

def data_analytics(request):

    context = {

    }

    return render(request, 'home/services/data-analytics.html', context)

def cloud_services(request):

    context = {

    }

    return render(request, 'home/services/cloud-services.html', context)

def iot_and_vr(request):

    context = {

    }

    return render(request, 'home/services/iot-and-vr.html', context)

#Indries vies
def education(request):

    context = {

    }

    return render(request, 'home/industries/education.html', context)

def real_estate(request):

    context = {

    }

    return render(request, 'home/industries/real-estate.html', context)

def construction(request):

    context = {

    }

    return render(request, 'home/industries/construction.html', context)

def healthcare(request):

    context = {

    }

    return render(request, 'home/industries/healthcare.html', context)

def robotics_and_ai(request):

    context = {

    }

    return render(request, 'home/industries/robotics-and-ai.html', context)

def e_commerce(request):

    context = {

    }

    return render(request, 'home/industries/e-commerce.html', context)

# Career views
def job_details_one(request):
    
    jobs = JobsApply.objects.all()
    for i in jobs:
        print(i.name)
    
    if request.method == 'POST':
        form = JobsApplyForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect(request.path_info)

        else:
            form = JobsApplyForm()
            
            messages.warning(request, 'Your application not submitted!')
            return redirect(request.path_info)
    
    else:
        form = JobsApplyForm()
    

    context = {

    }

    return render(request, 'home/career/job-details-one.html', context)


def job_details_two(request):
    
    
    if request.method == 'POST':
        form = JobsApplyForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect(request.path_info)

        else:
            form = JobsApplyForm()
            
            messages.warning(request, 'Your application not submitted!')
            return redirect(request.path_info)
    
    else:
        form = JobsApplyForm()
    
    
    
    context = {

    }

    return render(request, 'home/career/job-details-two.html', context)

