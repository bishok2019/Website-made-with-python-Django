from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Video
from home.models import Like
from home.models import Dislike
from home.models import Comment
from django.contrib import messages
from .models import Video
from .models import News  # Import the News model

# Create your views here.
def index(request):
    
    videos = Video.objects.all()
    my_dict = {"insert_me":"Hello! I am from views.py"}
    messages.success(request, "Welcome to our Bishok Multimedia")
    
   # return HttpResponse("this is home page")
    return render(request,'index.html', my_dict)
    
def about(request):
    # Retrieve all news objects
    news_list = News.objects.all()

    # Pass the news_list to the template
    return render(request, 'about.html', {'news_list': news_list})
    #return HttpResponse("this is about page")
    

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