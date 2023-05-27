
from django.http import HttpResponse
#to import HttpResponseRedirect
from django.http import HttpResponseRedirect

# Create your views here.
from django.shortcuts import render

#to import Student Table class from models.py
from flights.models import Flight

#to import class from forms.py
from . forms import AgentProfile

# Create your views here.
def Flight_Details(request):

    flight1 = ['USA', 'UK', 10]
    flight2 = ['Canada', 'Franch', 30]
    flight3 = ['USA', 'Germany', 40]
    flight4 = ['Franch', 'Germany', 70]
    flight5 = ['Italy', 'Norway', 120]

    flight_count = {'fg1' : flight1, 'fg2' : flight2, 'fg3' : flight3, 
                    
                    'fg4' : flight4, 'fg5' : flight5}

    return render(request,'flights/flightdetails.html', flight_count)

#table view for SQlite DB
def client_info(request):
    
    c_info = Flight.objects.all()

    return render(request, 'flights/clientsinfo.html', {'client' : c_info })

#for form API
#to import HttpResponseRedirect
from django.http import HttpResponseRedirect
def agent_info(request):

    #apply POST method on form to hide details from url while submitting 

    if request.method == "POST":

        agent_frm = AgentProfile(request.POST)

        if agent_frm.is_valid():
            #to show in terminal
            print(agent_frm)
            print('Execute POST')
            print(agent_frm.cleaned_data)
            print("Last_Name: ", agent_frm.cleaned_data['last_name'])
            print("First_name: ", agent_frm.cleaned_data['first_name'])
            print("email: ", agent_frm.cleaned_data['email'])
            print("password: ", agent_frm.cleaned_data['password'])
            print("re_password: ", agent_frm.cleaned_data['re_password'])

            #after submitting the form it will redirect successfully url
            return HttpResponseRedirect('/fl/successfully/')

    
    #if it is not POST method, it's GET method
    else:

        agent_frm = AgentProfile(auto_id= 'agent_%s', label_suffix=":", 
                             initial={'last_name' : 'your last name',
                                      'first_name':'your first name',
                                      'email': 'agents@email.com'}) #from forms.py
        
        #agent_frm.order_fields(field_order=['acode', 'Last_name', 'email','password', 'First_name', 'mobile', 'textarea', 'checkbox'])
        print("Execute GET Method")

    return render(request, 'flights/agentsinfo.html',{'agents' : agent_frm })

    


#submission html
def success(request):
    return render(request, 'flights/submit.html')
 