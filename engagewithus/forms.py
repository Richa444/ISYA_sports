from django import forms
from .models import Volunteer

class VolunteerForm(forms.ModelForm):
    class Meta:
     model = Volunteer
     fields =['first_name','last_name','email','phone','message']
     widgets ={ 
        'first_name': forms.TextInput(attrs={'class':'form-control'}),
        'last_name': forms.TextInput(attrs={'class':'form-control'}),
        'email': forms.EmailInput(attrs={'class':'form-control'}),
        'phone': forms.TextInput(attrs={'class':'form-control'}),
        'message': forms.Textarea(attrs={'class':'form-control'}),
     }
    