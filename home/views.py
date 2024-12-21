from django.shortcuts import render, redirect
from office.models import *
# Create your views here.
def index(request):

    return render(request, 'home/index.html')

def login(request):
    if request.session.has_key('owner_mobile'):
        return redirect('owner_home')
    if request.session.has_key('office_mobile'):
        return redirect('office_home')
    else:
        if request.method == "POST":
            number=request.POST ['number']
            pin=request.POST ['pin']
            o = Office_employee.objects.filter(mobile=number,pin=pin,status=1) 
            if o:
                request.session['office_mobile'] = request.POST["number"]
                return redirect('office_home')
            else:
                return redirect('/login/')
    return render(request, 'home/login.html')

def logout(request):
    if request.session.has_key('office_mobile'):
        del request.session['office_mobile']
    return redirect('login')