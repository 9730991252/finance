from django.urls import path
from . import views

urlpatterns = [
    path('account_holder_home/', views.account_holder_home, name='account_holder_home'),
]