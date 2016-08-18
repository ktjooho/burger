from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.template import loader
from django.contrib.auth import views,authenticate,login
from django.core.urlresolvers import reverse
import sys
from django.contrib.auth.decorators import login_required
from .models import User

#@login_required()
def index(request):
    context = {'is_authenticated':request.user.is_authenticated}
    print 'Auth:',request.user.is_authenticated
    print 'Pass :', sys.version
    if request.user.is_authenticated:
        print 'gg'
    else:
        print 'Nope'

    print 'index'
    #print reverse('angus:sign_up')
    #print 'index request:',request
    template = loader.get_template('angus/index.html')
    return HttpResponse(template.render(context,request))
def intro(request):
    return render(request,'angus/base.html')
def game(request):
    return render(request,'angus/game.html')
def login_success(request):
    #print 'LOGIN SUCESS',request
    template = loader.get_template('angus/login_success.html')
    return HttpResponse(template.render(request))
    #return HttpResponse('Login Success!!!!!')
def sign_in(request):
    plist = request.POST
    #print plist
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        return redirect(reverse('angus:login_success'))
        return HttpResponseRedirect(reverse('angus:login_success'))
        template = loader.get_template('angus/index.html')
        #print 'Template:',template
        x = template.render(request)
        #print 'x',x
        #print 'Login Successful!'
        return HttpResponseNotFound('<h1>What the hack!!</h1>')


        #return HttpResponseRedirect(reverse('angus:index'))
    else:
        return HttpResponse('Fail to LOgin')
        #print 'Doesn\'t exist id!'
        template = loader.get_template('angus/intro.html')
        return HttpResponseRedirect(template.render(request))
def sign_up(request):
    plist = request.POST
    #print type(plist)
    #print  plist
    #print len(plist)
    return render(request,'angus/sign_up.html')

# Create your views here.
