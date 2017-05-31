from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


# Create your views here.
variables = {}

class SignUpView(CreateView):
    template_name = 'core/signup.html'
    form_class = UserCreationForm

def main(request):
	if request.is_ajax():
		return render_to_response('social/test.html', variables)
	else:
		return render(request, 'social/main.html', {})