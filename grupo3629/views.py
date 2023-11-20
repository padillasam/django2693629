
from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse('<h1>Hola Mundo Django ADSO 2023')

def home(request):
    return render(request,'home.html')