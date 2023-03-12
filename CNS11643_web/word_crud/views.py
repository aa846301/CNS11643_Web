from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SreachWord
# Create your views here.

def word_view(request):
    return HttpResponse("hello world")

def index_view(request):
    return render(request,'word_crud/index.html')

def sreach_view(request):
    search_query = request.GET.get('search_field')
    if search_query == None:
        return render(request,'word_crud/search.html',{'search_query': search_query})
    return render(request,'word_crud/search_results.html',{'search_query': search_query})
