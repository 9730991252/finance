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
            'last_five_transaction':Saving_account.objects.filter(account_holder_id=a.id).order_by('-id')
        }
        return render(request, 'account_holder/account_holder_home.html', context)
    else:
        return redirect('login')