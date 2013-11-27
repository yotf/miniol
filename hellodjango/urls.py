from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('tt.urls',namespace="tt")),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^tt/',include('tt.urls',namespace="tt")),
                        

    
                       
)
