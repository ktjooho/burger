from django.conf.urls import url
from angus import views
app_name = 'angus'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^intro/$',views.intro,name='intro'),
]