from django.http import *
from django.shortcuts import *
from django.template.loader import *
from django.db.models import Q
from office.models import *

def search_account_holder(request):
    if request.method == 'GET':
        a = ''
        words = request.GET['words']
        if words:
            a = Account_holder.objects.filter(Q(holder_name__icontains=words)).order_by('holder_name')
    cotext={'a':a[0:3]}
    t = render_to_string('ajax/search_account_holder.html', cotext)
    return JsonResponse({'t':t})
