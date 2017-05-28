from django.shortcuts import render
from .forms import UserCreationForm, AuthenticationForm

# Create your views here.

def index(request):
	return render(request, 'home/index.html', {})

def login(request):
	form = AuthenticationForm()
	return render(request, 'home/login.html', {'form':form})

def signup(request):

	if request.method == "POST":
		signup_form = UserCreationForm(request.POST)
		if signup_form.is_valid:
			user = signup_form.save(commit=False)
			user.save()

			return render(request, 'home/signup_done.html', {'user':user})

	elif request.method == "GET":
		form = UserCreationForm()
	
	return render(request, 'home/signup.html', {'form':form})

