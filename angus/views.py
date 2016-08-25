from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.template import loader, RequestContext
from django.contrib.auth import views,authenticate,login
from django.core.urlresolvers import reverse
from angus.forms import  UserForm, UserProfileForm,GuestBookForm
from angus.models import GuestBook
from django.contrib.auth.decorators import login_required
from ipware.ip import get_real_ip



#@login_required('angus:login')
#@login_required(login_url='angus:login',redirect_field_name='intro') #Should refer to url name!
#@login_required(login_url='angus:login')
def guestbook(request):
    is_login = request.user.is_authenticated
    if request.method == 'POST':
        if is_login:
            author = request.user
        else:
            author = request.POST['author']

        content = request.POST['content']
        ip_address = get_real_ip(request)

        if ip_address is None:
            ip_address = "127.0.0.1"

        post = GuestBook(content=content,author=author,ip_address=ip_address)
        post.save()
        return HttpResponseRedirect(reverse('angus:index'))
    else :
        guestbook_form = GuestBookForm()
        context = {'guestbook_form':guestbook_form,'is_login':is_login,'user':request.user}
        return render(request,'angus/guestbook.html',context)
def index(request,redirect=None):
    print 'Args:',redirect
    context = {'is_authenticated':request.user.is_authenticated}
    #print reverse('angus:sign_up')
    #print 'index request:',request
    template = loader.get_template('angus/index.html')
    return HttpResponse(template.render(context,request))
#@login_required(login_url='angus:login',redirect_field_name='index')
def intro(request):
    return render(request,'angus/base.html')

def register(request):
    #context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        print 'Data:',user_form.data['password']
        fm = user_form.data['password']
        print 'fm type:',type(fm)

        profile_form = UserProfileForm(files=request.FILES)

        if user_form.checkValidPassword() and user_form.is_valid() and profile_form.is_valid():
            print 'Success to get qualifeid'
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else : #Handling error
            print 'Register Error:',user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {'user_form':user_form,'profile_form':profile_form,'registered':registered,}
    return render(request,'angus/register.html',context)
def game(request):
    return render(request,'angus/game.html')
def login_success(request):
    #print 'LOGIN SUCESS',request
    template = loader.get_template('angus/login_success.html')
    return HttpResponse(template.render(request))
    #return HttpResponse('Login Success!!!!!')
def sign_in(request,redirect=None):
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
def user_login(request,next=None):
    print 'User Login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user:
            print 'Yes it\'s user!'
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('angus'+next))
            else:
                return HttpResponse("Your account is disabled")
        else:
            print('Invalid Information')
            return HttpResponse("""
                <br>Invalid login information. please try again</br>
                <br>If you aren't a member. Please join our member.</br>
                <a href="/angus/register">register membership</a>
                                """
                                )
    else:
        print 'Input user '
        return render(request,'angus/user_login.html')

def sign_up(request):
    plist = request.POST
    #print type(plist)
    #print  plist
    #print len(plist)
    return render(request,'angus/sign_up.html')

# Create your views here.
