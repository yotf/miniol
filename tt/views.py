from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
from tt.models import Module,Aktivnost,ZavrseneAktivnosti,Updates
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    module_list = Module.objects.all()
    #module_list = [module.aktivnost_set.all() for module in module_list]
    completed_activity_list = get_object_or_404(ZavrseneAktivnosti,student=request.user.id).activity.all()
    progress = float(len(completed_activity_list))/float(len(Aktivnost.objects.all()))
    try:
        updates = get_list_or_404(Updates)[:5]
    except:
        updates = ["No updates yet"]
    context = {'module_list':module_list,
               'completed_activity_list':completed_activity_list,
                'progress':progress,
                'updates':updates}
    
    return render(request,'tt/index.djhtml',context)

def activity(request,url):
    activity = get_object_or_404(Aktivnost,url=url)

    return render(request,'tt/%s.djhtml' % url,{'activity':activity,'form':ActivityCompletedForm()})

def submit(request):
    form = ActivityCompletedForm(request.POST)
    if form.is_valid():
        activity_id = form.cleaned_data['activity_id']
        za = ZavrseneAktivnosti(student=1,activity=activity_id)
        za.save()

from django.contrib.auth import authenticate,login
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect(reverse('tt:index'))
        else:
            return HttpResponse("User inactive!")
    else:
        return HttpResponse("Bad login!")

    


def redirect_login(request):
    return render(request,'tt/login.djhtml')


    
    


    


