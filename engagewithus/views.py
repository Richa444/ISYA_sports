from django.shortcuts import render
from .forms import VolunteerForm
from .models import Volunteer

# Create your views here.

#def homeapptest(request):
    #return render(request, 'core/.html',{'title':'this is test'})



def volunteer(request):
    if request.method == 'POST': 
      fm = VolunteerForm(request.POST)
      if fm.is_valid():
        fm.save()
        fm = VolunteerForm()
    else: 
      fm = VolunteerForm()
    return render(request, 'engagewithus/volunteer.html',{'form':fm})

def what_they_say(request):
    return render(request,'engagewithus/whattheysay.html') 

def show_volunteer(request):      
    vol = Volunteer.objects.all()
    return render(request,'engagewithus/show_volunteer.html',{'volunteer':vol}) 


