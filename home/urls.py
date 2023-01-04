#home urls
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    
    #home urls
    path('', views.index, name='index'),
    path('contact-us/', views.contact, name='contact'),
    path('about-us/', views.about, name='about'),
    path('case-studies/', views.case_studies, name='case_studies'),
    path('career/', views.career, name='career'),
   
    #ajax form submission
    path('ajax/contact/', views.ajax_contact, name='ajax_contact'),

    #services urls
    path('medical-solution/', views.medical_solution, name='medical_solution'),
    path('mobile-app/', views.mobile_app, name='mobile_app'),
    path('erp-solution/', views.erp_solution, name='erp_solution'),
    path('e-commerce-solution/', views.e_commerce_solution, name='e_commerce_solution'),
    path('cyber-security/', views.cyber_security, name='cyber_security'),
    path('data-analytics/', views.data_analytics, name='data_analytics'),
    path('iot-and-vr/', views.iot_and_vr, name='iot_and_vr'),
    path('cloud-services/', views.cloud_services, name='cloud_services'),

    #industries urls
    path('healthcare/', views.healthcare, name='healthcare'),
    path('education/', views.education, name='education'),
    path('real-estate/', views.real_estate, name='real_estate'),
    path('construction/', views.construction, name='construction'),
    path('robotics-and-ai/', views.robotics_and_ai, name='robotics_and_ai'),
    path('e-commerce/', views.e_commerce, name='e_commerce'),

    #career urls
    path('jobs/python-developer-intern/', views.job_details_one, name='job_details_one'),
    path('jobs/python(djnago)-developer/', views.job_details_two, name='job_details_two'),

    #Dashboard urls
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/apply/delete/<pk>/', views.jobs_apply_delete, name='jobs_apply_delete'),
    
]