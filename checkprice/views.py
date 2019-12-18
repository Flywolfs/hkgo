from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def search_item(request):

    if request.method == 'POST' :
        pass
    ctx={"name":"","cn_official_price":"","hk_official_price":"","other_people_price":"","our_price":"","pic":""}
    return render(request,"search.html",{"data":ctx})

def record_item(request):
    pass