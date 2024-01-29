from SCproject.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
import razorpay



# Create your views here.
def test(request):
    return render(request, 'core/test.html',{'title':'this is test'})

def home(request):
    return render(request, 'core/home.html',{'title':'this is home page'})

def header(request):
    return render(request, 'core/header.html')

def contact(request):
    if request.method == 'POST': 
      fm = ContactForm(request.POST)
      if fm.is_valid():
        fm.save()
        fm = ContactForm()
    else: 
      fm = ContactForm()
      con = Contact.objects.all()
    return render(request, 'core/contact.html',{'form':fm,'contact':con})

 
 #fm = ContactForm(auto_id=True, label_suffix='')  
def show_contact(request):      
    con = Contact.objects.all()
    return render(request,'core/show_contact.html', {'contact':con}) 


   
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def donate(request):
 
    order_amount = 50000 
    order_currency = 'INR'
    payment_order = client.order.create(dict(amount = order_amount, currency = order_currency , payment_capture = 1))
    payment_order_id = payment_order['id']
    
    
    context = {
        'amount': 500,
        'api_key': RAZORPAY_API_KEY,
        'order_id': payment_order_id
    }
    # Handle the donation logic here
    return render(request, 'core/donate.html', context)