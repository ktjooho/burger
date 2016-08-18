from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from angus import views
from angus.forms import LoginForm
from django.contrib.auth.decorators import login_required

app_name = 'angus'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^intro/$',views.intro,name='intro'),
    url(r'^game/$',views.game,name='game'),
    url(r'^signup/$',views.sign_up,name='sign_up'),
    url(r'^signin/$',views.sign_in,name='sign_in'),
    url(r'^login_sucess/$',views.login_success,name='login_success'),
    url(r'^login/$', auth_views.login, {'template_name': 'angus/login.html', 'authentication_form': LoginForm},name='login'),
    url(r'^logout/$',auth_views.logout,{'next_page':'angus:index'},name='logout'),
]
