from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    response=requests.get('https://api.covid19api.com/countries').json()
    return render(request,'home.html',{'response':response})