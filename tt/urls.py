from django.conf.urls import patterns, url

from tt import views

urlpatterns = patterns('',
                       url(r'^$',views.index,name='index'),
                       url(r'^(?P<url>\w+)/$',views.activity,name='activity')
                       )