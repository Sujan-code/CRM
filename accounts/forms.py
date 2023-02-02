from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CustomerForm(ModelForm): #setting ma banako form
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']

class OrderForm(ModelForm): #model ko naamaniform  inline form ho ta?
	class Meta:
		model = Order #kun model ko lagi form banako ho
		fields = '__all__'


class CreateUserForm(UserCreationForm): #register 
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
