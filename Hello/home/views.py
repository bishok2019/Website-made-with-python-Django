from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Video
from home.models import Like
from home.models import Dislike
from home.models import Comment
from django.contrib import messages
# Create your views here.
def index(request):
    my_dict = {"insert_me":"Hello! I am from views.py"}
    messages.success(request, "Welcome to our Bishok Multimedia")
   # return HttpResponse("this is home page")
    return render(request,'index.html', my_dict)
    
def about(request):
    
    #return HttpResponse("this is about page")
    return render(request,'about.html')

def contact(request):
    #return HttpResponse("this is contact page")
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name = name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request,'Message has bees Sent!')
    return render(request,'contact.html')

def service(request):
    #return HttpResponse("this is service page")
    return render(request,'service.html')