from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def search_item(request):
    return render(request,"search.html")

def record_item(request):
    pass