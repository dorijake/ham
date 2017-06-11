# from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from django.http import JsonResponse

class SignUpView(CreateView):
    template_name = 'ajaxapp/signup.html'
    form_class = UserCreationForm


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
    	'is_success': '1',
    	'username': "hey"
        # 'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    print("what")
    return JsonResponse(data)

# from django.shortcuts import render
 
# def iindex(request):
#     msg = 'My Message'
#     return render(request, 'ajaxapp/index.html', {'message': msg})