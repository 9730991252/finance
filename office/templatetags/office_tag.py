from django import template
from office.models import *
from django.db.models import Avg, Sum, Min, Max
from math import *
import math
from datetime import date
register = template.Library()
@register.simple_tag()
def account_holder_available_balence(account_holder_id):
    credit = Saving_account.objects.filter(account_holder_id=account_holder_id).aggregate(Sum('credit_amount'))
    debit = Saving_account.objects.filter(account_holder_id=account_holder_id).aggregate(Sum('debit_amount'))
    if credit['credit_amount__sum'] is None:
        credit['credit_amount__sum'] = 0
    if debit['debit_amount__sum'] is None:
        debit['debit_amount__sum'] = 0
    total_avalable_balence = (credit['credit_amount__sum'] - debit['debit_amount__sum'])
    return total_avalable_balence

@register.simple_tag()
def account_holder_pending_loan(account_holder_id):
    loan = Loan.objects.filter(account_holder_id=account_holder_id, loan_status=1).aggregate(Sum('loan_amount'))
    return loan['loan_amount__sum']

@register.inclusion_tag('inclusion_tag/office/todays_collection.html')
def todays_collection():
    todays_collection = Saving_account.objects.filter(date=date.today()).aggregate(Sum('credit_amount'))
    o = Office_employee.objects.filter(status=1)
    office_employee = []
    for i in o:
        a = Saving_account.objects.filter(date=date.today(), collected_by_id=i.id).aggregate(Sum('credit_amount'))
        a = a['credit_amount__sum']
        if a is None:
            a = 0
        office_employee.append({
            'name': i.name,
            'credit_amount': a
        })
    return {
        'todays_collection': todays_collection['credit_amount__sum'],
        'office_employee': office_employee
        }
    
@register.inclusion_tag('inclusion_tag/office/summary.html')
def summary():
    total_account_holder = Account_holder.objects.all().count()
    total_collection = Saving_account.objects.aggregate(Sum('credit_amount'))
    total_withdrawal = Saving_account.objects.aggregate(Sum('debit_amount'))
    total_office_employee = Office_employee.objects.filter(status=1).count()
    loan_amount_pending = Loan.objects.filter(loan_status=1).aggregate(Sum('loan_amount'))
    if total_collection['credit_amount__sum'] is None:
        total_collection['credit_amount__sum'] = 0
    if total_withdrawal['debit_amount__sum'] is None:
        total_withdrawal['debit_amount__sum'] = 0
    avalable_amount = total_collection['credit_amount__sum'] - total_withdrawal['debit_amount__sum']
    return {
        'total_account_holder': total_account_holder,
        'total_withdrawal': total_withdrawal['debit_amount__sum'],
        'total_office_employee': total_office_employee,
        'loan_amount_pending': loan_amount_pending['loan_amount__sum'],
        'avalable_amount': avalable_amount
    }
@register.inclusion_tag('inclusion_tag/office/todays_withdrawal.html')
def todays_withdrawal():
    todays_collection = Saving_account.objects.filter(date=date.today()).aggregate(Sum('debit_amount'))
    o = Office_employee.objects.filter(status=1)
    office_employee = []
    for i in o:
        a = Saving_account.objects.filter(date=date.today(), collected_by_id=i.id).aggregate(Sum('debit_amount'))
        a = a['debit_amount__sum']
        if a is None:
            a = 0
        office_employee.append({
            'name': i.name,
            'debit_amount': a
        })
    return {
        'todays_withdrawal': todays_collection['debit_amount__sum'],
        'office_employee': office_employee
        }