from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import time
# Create your views here.
def office_home(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=mobile).first()
        context={
            'e':e,
        }
        return render(request, 'office/office_home.html', context)
    else:
        return redirect('login')
    
def account_holder_details_loan(request, id):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=mobile).first()
        if e:
            if 'add_loan'in request.POST:
                print('hi')
                loan_amount = request.POST.get('loan_amount')
                interest_percentage = request.POST.get('interest_percentage')
                minimum_installment = request.POST.get('minimum_installment')
                if Loan.objects.filter(account_holder_id=id, loan_status=1).exists():
                    messages.warning(request, f"Loan already exists with this खातेदार")
                else:
                    Loan(
                        loaned_by_id=e.id,
                        account_holder_id=id,
                        loan_amount=loan_amount,
                        interest_percentage=interest_percentage,
                        minimum_installment=minimum_installment,
                    ).save()
                    Saving_account(
                        collected_by_id=e.id,
                        account_holder_id=id,
                        credit_amount=loan_amount,
                        remark='Loan Credit',
                    ).save()
                return redirect(f'/office/account_holder_details_loan/{id}')
        else:
            return redirect('login')
        context={
            'e':e,
            'account_holder':Account_holder.objects.filter(id=id).first(),
            'last_five_transaction':Saving_account.objects.filter(account_holder_id=id).order_by('-id')[:5],
            'loan':Loan.objects.filter(account_holder_id=id, loan_status=1).first(),
        }
        return render(request, 'office/account_holder_details_loan.html', context)
    
def loan(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=mobile).first()
        if e:
            pass
        else:
            return redirect('login')
        context={
            'e':e,
            # 'loan':Loan.objects.all(),
            'account_holder':Account_holder.objects.all(),
        }
        return render(request, 'office/loan.html', context)
    else:
        return redirect('login')
    
def account_holder_details_withdrawal(request, id):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=mobile).first()
        if e:
            if 'Withdraw_amount'in request.POST:
                withdraw_amount = request.POST.get('withdraw_amount')
                Saving_account(
                    collected_by_id=e.id,
                    account_holder_id=id,
                    debit_amount=withdraw_amount,
                    remark='Withdraw',
                ).save()
                return redirect(f'/office/account_holder_details_withdrawal/{id}')
        else:
            return redirect('login')
        context={
            'e':e,
            'account_holder':Account_holder.objects.filter(id=id).first(),
            'last_five_transaction':Saving_account.objects.filter(account_holder_id=id).order_by('-id')[:5],
        }
        return render(request, 'office/account_holder_details_withdrawal.html', context)
    
def withdrawal(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=mobile).first()
        if e:
            pass
        else:
            return redirect('login')
        context={
            'e':e,
            'account_holder':Account_holder.objects.all(),
        }
        return render(request, 'office/withdraw.html', context)
    else:
        return redirect('login')
    
def account_holder_details_collection(request, id):
    if request.session.has_key('office_mobile'):
        momile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=momile).first()
        if e:
            if 'Collect_amount'in request.POST:
                credit_amount = request.POST.get('credit_amount')
                Saving_account(
                    collected_by_id=e.id,
                    account_holder_id=id,
                    credit_amount=credit_amount,
                    remark='Collection',
                ).save()
                return redirect(f'/office/account_holder_details_collection/{id}')
        else:
            return redirect('login')
        context={
            'e':e,
            'account_holder':Account_holder.objects.filter(id=id).first(),
            'last_five_transaction':Saving_account.objects.filter(account_holder_id=id).order_by('-id')[:5],
        }
        return render(request, 'office/account_holder_details_collection.html', context)
    
def collection(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=mobile).first()
        context={
            'e':e,
        }
        return render(request, 'office/collection.html', context)
    else:
        return redirect('login')
    
def employee(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=mobile).first()
        if e:
            if 'Add_employee'in request.POST:
                name = request.POST.get('name')
                mobile = request.POST.get('mobile')
                pin = request.POST.get('pin')
                if Office_employee.objects.filter(mobile=mobile).exists():
                    messages.warning(request, f"Employee already exists with mobile number - {mobile}")
                else:
                    Office_employee(
                        added_by_id=e.id,
                        name=name,
                        mobile=mobile,
                        pin=pin,
                    ).save()
                return redirect('employee')
            if 'Edit_employee'in request.POST:
                id = request.POST.get('id')
                name = request.POST.get('name')
                mobile = request.POST.get('mobile')
                pin = request.POST.get('pin')
                o = Office_employee.objects.filter(id=id).first()
                if Office_employee.objects.filter(mobile=mobile).exclude(id=id).exists():
                    messages.warning(request, f"Employee already exists with mobile number - {mobile}")
                else:
                    o.name = name
                    o.mobile = mobile   
                    o.pin = pin
                    o.save()
                if o.id == e.id:
                    del request.session['office_mobile']
                    return redirect('login')
                return redirect('employee')
            if 'active'in request.POST:
                id = request.POST.get('id')
                c = Office_employee.objects.filter(id=id).first()
                c.status = 0
                c.save()
                return redirect('employee')
            if 'deactive'in request.POST:
                id = request.POST.get('id')
                c = Office_employee.objects.filter(id=id).first()
                c.status = 1
                c.save()
                return redirect('employee')
        else:
            return redirect('login')
        context={
            'e':e,
            'employee':Office_employee.objects.all(),
        }
        return render(request, 'office/employee.html', context)
    else:
        return redirect('login')

def account_holder(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=mobile).first()
        if e:
            if 'Add_account_holder'in request.POST:
                holder_name = request.POST.get('holder_name')
                mobile = request.POST.get('mobile')
                pin = request.POST.get('pin')
                address = request.POST.get('address')
                if Account_holder.objects.filter(mobile=mobile).exists():
                    messages.warning(request, f"खातेदार already exists with mobile number - {mobile}")
                else:
                    Account_holder(
                        holder_name=holder_name,
                        mobile=mobile,
                        pin=pin,
                        address=address,
                    ).save()
                return redirect('account_holder')
            if 'Edit_account_holder'in request.POST:
                id = request.POST.get('id')
                holder_name = request.POST.get('holder_name')
                mobile = request.POST.get('mobile')
                pin = request.POST.get('pin')
                address = request.POST.get('address')
                a = Account_holder.objects.filter(id=id).first()
                if Account_holder.objects.filter(mobile=mobile).exclude(id=id).exists():
                    messages.warning(request, f"खातेदार already exists with mobile number - {mobile}")
                else:
                    a.holder_name = holder_name
                    a.mobile = mobile   
                    a.pin = pin
                    a.address = address
                    a.save()
                return redirect('account_holder')
            if 'active'in request.POST:
                id = request.POST.get('id')
                c = Account_holder.objects.filter(id=id).first()
                c.status = 0
                c.save()
                return redirect('account_holder')
            if 'deactive'in request.POST:
                id = request.POST.get('id')
                c = Account_holder.objects.filter(id=id).first()
                c.status = 1
                c.save()
                return redirect('account_holder')
        else:
            return redirect('login')
        context={
            'e':e,
            'account_holder':Account_holder.objects.all(),
        }
        return render(request, 'office/account_holder.html', context)
    else:
        return redirect('login')