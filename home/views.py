from django.shortcuts import render

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

    context = {

    }
    
    return render(request, 'home/contact.html', context)

def case_studies(request):

    context = {

    }

    return render(request, 'home/case-studies.html', context)
    