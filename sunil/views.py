from django.shortcuts import redirect, render
from office. models import *
# Create your views here.
def sunil_login(request):
    if request.method == 'POST':
        a =int(request.POST["number"])
        b =int(request.POST["pin"])
        s = a+b
        if s == 11000 :
            request.session['sunil_mobile'] = s
            return redirect('sunil_home')
        else:
            return redirect('sunil_login')
    return render(request, 'sunil/sunil_login.html')


def sunil_home(request):
    if request.session.has_key('sunil_mobile'):
        if 'Add_employee'in request.POST:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            if Office_employee.objects.filter(mobile=mobile).exists():
                pass
            else:
                Office_employee(
                    name=name,
                    mobile=mobile,
                    pin=pin,
                ).save()    
            return redirect('sunil_home')
        if 'Edit_employee'in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            o = Office_employee.objects.filter(id=id).first()
            o.name = name
            o.mobile = mobile   
            o.pin = pin
            o.save()
            return redirect('sunil_home')
        if 'active'in request.POST:
            id = request.POST.get('id')
            c = Office_employee.objects.filter(id=id).first()
            c.status = 0
            c.save()
            return redirect('sunil_home')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            c = Office_employee.objects.filter(id=id).first()
            c.status = 1
            c.save()
            return redirect('sunil_home')
        context={
            'employee':Office_employee.objects.all(),
        }
        return render(request, 'sunil/sunil_home.html', context)
    else:
        return redirect('sunil_login')