from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('angus/index.html')
    return HttpResponse(template.render(request))
    #return HttpResponse(request)
    #return render(request,'index.html')
def intro(request):
    return render(request,'angus/intro.html')

# Create your views here.
