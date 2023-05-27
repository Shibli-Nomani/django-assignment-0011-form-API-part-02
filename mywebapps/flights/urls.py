from django.urls import path
from . import views

urlpatterns = [
    path('flightdetails/', views.Flight_Details, name ='flights'),
    path('clientdetails/', views.client_info, name ='client_details'),
    path('agentdetails/', views.agent_info, name ='agent_details'),
    path('successfully/',views.success, name = 'successfully'),
    
   
]