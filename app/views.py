from django.shortcuts import render

# Create your views here.

def looping(request):
    d={'name':'subash','L':[10,20,25,35]}
    return render(request,'looping.html',d)