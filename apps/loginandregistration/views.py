from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User
# Create your views here.
def index(request):
	return render(request, "loginandregistration/index.html")

def register(request):
	if request.method == 'POST':
		if User.userManager.register(request):		# successful registration
			return redirect("/dashboard")
		else: 										# failed registration
			return redirect("/register")
	else:
		if 'id' in request.session:
			return redirect("/dashboard")
		return render(request, "loginandregistration/registration.html")

def login(request):
	# POST
	if request.method == 'POST':
		if User.userManager.login(request):	# successful login
			return redirect("/dashboard")
		else: 										# failed login
			return redirect("/signin")
	# GET
	else: 
		if 'id' in request.session:
			return redirect("/dashboard")
		return render(request, "loginandregistration/login.html")

def logoff(request):
	User.userManager.logoff(request)								# failed login
	return redirect("/")