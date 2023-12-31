from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Video
from home.models import Like
from home.models import Dislike
from home.models import Comment
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Video
from .models import News  # Import the News model
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username=username, password=password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.email = email
        myuser.save()

        messages.success(request, "Registration Success!")
        return redirect(signin)
    # message={"hello":"welcome"}
    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (username = username , password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            request.session.save()
            return render(request,"index.html",{'username': username})
        else:
            messages.error(request,"Bad request")
            return redirect(signin)
    return render(request, "signin.html")


def index(request):
    my_dict = {"insert_me":"Hello! I am from views.py"}
    messages.success(request, "Welcome to Bishok Multimedia")
    
   # return HttpResponse("this is home page")
    return render(request,'index.html', my_dict)
    
def about(request):
    # Retrieve all news objects
    about_list = News.objects.all()

    # Pass the news_list to the template
    return render(request, 'about.html', {'about_list': about_list})
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
    videos = Video.objects.all()
    #return HttpResponse("this is service page")
    return render(request,'service.html',{'videos': videos})


def signout(request):
    logout(request)
    messages.success(request, "Logged Out successfully!")
    return render(request,'signin.html')