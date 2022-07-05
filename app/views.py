from django.shortcuts import render, HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse('Welcome Home') 

def home(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')
