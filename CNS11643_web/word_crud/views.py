from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import WordModels

# Create your views here.

def word_view(request):
    return HttpResponse("hello world")

def index_view(request):
    return render(request,'word_crud/index.html')

def sreach_view(request):
    #取得輸入值
    search_query = request.GET.get('search_field')
    #print(search_query)
    #檢查字元長度
    if len(search_query) == 1:
        #將輸入值轉UNICODE
        word_uni = hex(ord(search_query))[2:].upper()
        #尋找資料庫
        CharMaps = WordModels.objects.filter(unicode_code=word_uni)
        if CharMaps.count()>0:
            #有對應資料
            return render(request,'word_crud/search_results.html',{'CharMaps': CharMaps})
        else:
            #無對應資料
            return render(request,'word_crud/search.html',{'search_query': search_query})
    else:
        return render(request,'word_crud/search.html',{'search_query': search_query})
    if search_query == "":
        return render(request,'word_crud/search.html',{'search_query': search_query})


