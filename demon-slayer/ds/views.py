# made by me
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import pyrebase


context = {'user': None}
config= {
    "apiKey": "AIzaSyBcfDC6VHKgcojkWrN2p4oXuI500-koI30",
    "authDomain": "test-7b70d.firebaseapp.com",
    "databaseURL": "https://test-7b70d-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "test-7b70d",
    "storageBucket": "test-7b70d.appspot.com",
    "messagingSenderId": "761698859336",
    "appId": "1:761698859336:web:cad6f078fcc44aa1b55b7d",
    "measurementId": "G-SXP78VSD2W"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def index(request):
    return render(request,'home.html', context)


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

        try:
            user = auth.create_user_with_email_and_password(email, pass1)
            messages.success(request,'Your account has been created successfully')
        except:
            messages.error(request, "email already exists")
        return render(request, 'home.html', context)
    else:
        return HttpResponse('404 not found')
      

def accin (request):
    if request.method=="POST":
        # Get the post parameters
        mailer=request.POST['mailer']
        password1=request.POST['password1']

        try:
            login_res = auth.sign_in_with_email_and_password(mailer, password1)
            context = {'user': mailer}
            messages.success(request, "Successfully Logged In")
            return render(request, 'home.html', context)

        except:
            messages.error(request, "Invalid credentials! Please try again")
            context = {'user': None}
            return render(request,'home.html', context)

    return HttpResponse(" 😓😓 404- Not found")

def accout(request):
    auth.current_user = None
    messages.success(request, "Successfully logged out")
    return redirect('/')