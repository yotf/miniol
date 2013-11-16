from django.conf.urls import patterns, url

from tt import views


urlpatterns = patterns('',
                       url(r'^$',views.index,name='index'),
                       url(r'^login$',views.redirect_login,name="redirect_login"),
                       url(r'^user_login$',views.user_login,name="user_login"),
                       url(r'^(?P<url>\w+)/$',views.activity,name='activity'),
                       url(r'^submit$',views.submit, name='submit')
                       )