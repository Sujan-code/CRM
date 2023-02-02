from django.http import HttpResponse
from django.shortcuts import redirect
#decorator is a function which takes another function as parameter and original fuction call hunuvanda pahila extra functionalities addd garna dinxa
#wrapper functiion execute vayapaxi matra execute hunxa
def unauthenticated_user(view_func): #view_func is login page
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home') #login xa vane home dekhaidine natra view func/login fuction ma jaa vanne
		else:
			return view_func(request, *args, **kwargs) #argument and keyword argument

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists(): #check user group
				group = request.user.groups.all()[0].name #group admin customer

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'customer':
			return redirect('user-page')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function