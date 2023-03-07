from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def word_test(request):
    return HttpResponse("hello world")

def word_search(request):
    return render(request,'word_crud/index.html')