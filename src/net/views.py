from django.shortcuts import render

# Create your views here.

def network(request):
	return render(request, 'net/network.html', {})
