from django.shortcuts import render,redirect, get_object_or_404
from tt.models import Module,Aktivnost


def index(request):
    module_list = Module.objects.all()
    #module_list = [module.aktivnost_set.all() for module in module_list]

    context = {'module_list':module_list}
    return render(request,'tt/index.djhtml',context)

def activity(request,url):
    return render(request,'tt/%s.djhtml' % url,{'test':'test'})


    