from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def hello1(request):
    return render(request, "hello.html", {})

def stores_list(request):
    return render(request, 'store.html', {})

