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
db=firebase.database()

# Create your views here.
def contact(request):
    return render(request,"cont.html")

def sender(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['msg']
        data={'name': name, 'email':email, 'message':msg}
        db.child("feedbacks").child(name).set(data)
        return redirect('/')

