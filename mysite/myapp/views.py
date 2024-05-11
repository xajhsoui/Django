from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import json
from django.template import loader
from django.shortcuts import render

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    List = ['orange', 'tomoto']
    Dict = {'name': 'Test', 'age': '40'}
    #template = loader.get_template('myapp/home.html')

    context = {
        'List': json.dumps(List),
        'Dict': json.dumps(Dict)
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)
 
def home(request):
    List = ['apple', 'banana']
    Dict = {'name': 'cao rui', 'age': '35'}
    #template = loader.get_template('myapp/home.html')

    context = {
        'List': json.dumps(List),
        'Dict': json.dumps(Dict)
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'home.html', context)

def home1(request):
    return render(request, 'home.html')