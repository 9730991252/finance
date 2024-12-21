from django.urls import path
from . import views

urlpatterns = [
    path('office_home/', views.office_home, name='office_home'),
    path('employee/', views.employee, name='employee'),
    path('account_holder/', views.account_holder, name='account_holder'),
    path('collection/', views.collection, name='collection'),
    path('account_holder_details_collection/<int:id>', views.account_holder_details_collection, name='account_holder_details_collection'),
    path('withdrawal/', views.withdrawal, name='withdrawal'),
    path('account_holder_details_withdrawal/<int:id>', views.account_holder_details_withdrawal, name='account_holder_details_withdrawal'),
    path('loan/', views.loan, name='loan'),
    path('account_holder_details_loan/<int:id>', views.account_holder_details_loan, name='account_holder_details_loan'),
]
