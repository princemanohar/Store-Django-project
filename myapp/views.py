from django.shortcuts import render
from django.http import JsonResponse, QueryDict
from django.core import serializers
from django.views.generic import View


import json
from .models import Store, Inventories, Reviews, Entities

# Create your views here.
from django.http import HttpResponse

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def hello1(request):
    return render(request, "hello.html", {})

def stores_list(request):
    allStores = Store.objects.all()
    data = serializers.serialize('json', allStores)
    data = json.loads(data)

    final_data = []
    for data1 in data:
        final_data.append(data1['fields'])

    return JsonResponse(final_data, safe=False)
    #return render(request, 'store.html', {})



class StoreView(View):
    def get(self, request, *args, **kwargs):
        allStores = Store.objects.all()
        data = serializers.serialize('json', allStores)
        data = json.loads(data)

        final_data = []
        for data1 in data:
            final_data.append(data1['fields'])

        return JsonResponse(final_data, safe=False)

    '''
        Create a Store entry
    '''
    def post(self, request, *args, **kwargs):
        print("POST Data : %s:" % request.POST)
        print("Body : %s:" % request.body)
        # Converting body to json object
        body = json.loads(request.body)
        createResp = Store.objects.create(
            **body
        )
        print("createResp: %d " % createResp.store_id)
        print (body)
        return JsonResponse(createResp.store_id, safe=False)


'''
Below View will be for a list of stores
'''
class StoresListView(View):
    def get(self, request, *args, **kwargs):
        allStores = Store.objects.all()
        data = serializers.serialize('json', allStores)
        data = json.loads(data)

        final_data = []
        for data1 in data:
            final_data.append(data1['fields'])

        return JsonResponse(final_data, safe=False)



