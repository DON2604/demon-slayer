# made by me
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'home.html')

def reg(request):
    return render(request, 'reg.html')

def handleSignup(request):
    if request.method == 'POST':


    else:
        return HttpResponse('404 not found')
