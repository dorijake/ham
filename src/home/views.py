from django.shortcuts import render
from .forms import UserCreationForm, AuthenticationForm
from user.forms import UserProfileForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from user.models import User

# Create your views here.

def index(request):
	return render(request, 'home/index.html', {})

def login(request):
	form = AuthenticationForm()
	return render(request, 'home/login.html', {'form':form})

def signup(request):

	if request.method == "POST":
		signup_form = UserCreationForm(request.POST)
		if signup_form.is_valid():

			# Put off saving user data into database until the user feed extra information on the next page.

			user = signup_form.save()

			redirect_to = reverse('extra_info', kwargs={'userid':user.id})

			return HttpResponseRedirect(redirect_to)
		else:

			return render(request, 'home/signup.html', {'form':signup_form})
	
	signup_form = UserCreationForm()
	
	return render(request, 'home/signup.html', { 'form':signup_form })


def extra_info(request, userid):

	if request.method == "POST":
		try:
			user = User.objects.get(pk=userid)
			form = UserProfileForm(request.POST or None, instance=user)

		except User.DoesNotExist:
			raise Http404("User does not exist.")

		if form.is_valid():

			form.save()

			return HttpResponseRedirect(reverse('signup_done'))
				
	form = UserProfileForm()

	return render(request, 'home/extra_info.html', {'form':form})



def signup_done(request):

	return render(request, 'home/signup_done.html', {})

