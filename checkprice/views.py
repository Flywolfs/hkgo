from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def search_item(request):

    if request.method == 'POST' and len(request.POST) == 1 and "item_name" in request.POST:
        print("enter search item!"+request.POST.get("item_name"))
        ctx = {"name": "xxx", "cn_official_price": "xxx", "hk_official_price": "xxx", "other_people_price": "xxx", "our_price": "xxx",
               "pic": "xxx"}
        return JsonResponse(ctx)
    elif request.method == 'GET':
        return render(request,"search.html")

def record_item(request):
    pass