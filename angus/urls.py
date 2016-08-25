from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from angus import views
from angus.forms import LoginForm,UserForm
from django.contrib.auth.decorators import login_required

app_name = 'angus'

urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^intro/$',views.intro,name='intro'),
    url(r'^game/$',views.game,name='game'),
    url(r'^signup/$',views.sign_up,name='sign_up'),
    url(r'^signin/$',views.sign_in,name='sign_in'),
    url(r'^login_sucess/$',views.login_success,name='login_success'),
    url(r'^login/$', auth_views.login, {'template_name': 'angus/user_login.html', 'authentication_form': LoginForm},name='login'),
    url(r'^logout/$',auth_views.logout,{'next_page':'angus:index'},name='logout'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,{'next':'index'},name='direct_login'),
    url(r'^user_login_(?P<next>[a-z]+)/$',views.user_login,name='redirect_login'),
    url(r'^guestbook/$',views.guestbook,name='guestbook'),
    
]
# Kwargs -> keyword, Dictionary.
# It is going to be arguemnts in view function!
