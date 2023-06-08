# made by me
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request,'home.html')

def reg(request):
    return render(request, 'reg.html')

def accr(request):
    if request.method == "POST":
        uname = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #checks
        if len(uname) < 3:
            messages.error(request, "Username must be at least more than 3 chararcters")
            return redirect('/')

        if pass1 != pass2:
            messages.error(request, "Passwords did not match")
            return redirect('/')
        
        if not uname.isalnum():
            messages.error(request, "Passwords must contain only letters and numbers")
            return redirect('/')        


        myuser = User.objects.create_user(uname, email, pass1)
        myuser.save()
        messages.success(request,'Your account has been created successfully')
        return redirect('/')
    else:
        return HttpResponse('404 not found')
    

def accin (request):
    if request.method=="POST":
        # Get the post parameters
        Username=request.POST['Username']
        password1=request.POST['password1']

        user=authenticate(username= Username, password= password1)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('/')

    return HttpResponse("404- Not found")

def accout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')