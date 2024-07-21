from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def home(request):
    return render(request,'play/index.html')

def signup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['Email']
        Password = request.POST['Password']
        Confirm_password = request.POST['Confirm_password']
        
        if User.objects.filter(username= username):
            messages.error(request,'Username already Exits.Please try another')
            return redirect('home')
            
        if User.objects.filter(email=email):
            messages.error(request,'Email already registered')
            return redirect('home')
                
        if len(username)>10:
            messages.error(request,'Username must be under 10 characters')
            
        if Password != Confirm_password:
            messages.error(request,"Passwords didn't match")
            
        if not username.isalnum():
            messages.error(request,"User Name must be alpha-numeric")  
            return redirect('home')  
                
        myuser = User.objects.create_user(username, email, Password)    
        
        myuser.save()

        messages.success(request, "Your Account has been successfully created")
        
        return redirect('login_')
    
    return render(request, 'play/signup.html')

def login_(request):
    if request.method == "POST":
        username = request.POST['username']
        Password = request.POST['Password']
        
        user= authenticate(username=username, password=Password)
        
        if user is not None:
            login(request, user)
            username = user.username
            return render(request,"play/index.html",{'username': username})
        
        else:
            messages.error(request,"Bad credentials")
            return redirect('home')    
    return render(request,'play/login.html')

def logout_(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('home')
