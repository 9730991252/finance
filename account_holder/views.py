from django.shortcuts import render
from django.shortcuts import redirect
from office.models import *
# Create your views here.
def account_holder_home(request):
    if request.session.has_key('account_holder_mobile'):
        mobile = request.session['account_holder_mobile']
        a = Account_holder.objects.filter(mobile=mobile).first()
        context={
            'a':a,
        }
        return render(request, 'account_holder/account_holder_home.html', context)
    else:
        return redirect('login')