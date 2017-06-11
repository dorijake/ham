from django.shortcuts import render

# Create your views here.
def graphtest(request):
    return render(request, 'graph/graph.html')