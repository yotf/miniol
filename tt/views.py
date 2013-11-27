from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
from tt.models import Module,Aktivnost,ZavrseneAktivnosti,Updates,Comment
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth import logout


def index(request):
    # da li ovde moze nesto da se desi???
    # treba da proverim da li je user
    # authenticated request.user.is_authenticated()
    if request.method!= 'GET':
        raise Http404()
    module_list = Module.objects.all()
    # if not request.user.is_authenticated():
    #     completed_activity_list = []
    # else:
    #     student = request.user.id
    #     zavrsenaAktivnost = get_object_or_404(ZavrseneAktivnosti,student=student)
    #     completed_activity_list = zavrsenaAktivnost.activity.all()
    # progress = float(len(completed_activity_list))/float(len(Aktivnost.objects.all())) if len(Aktivnost.objects.all())!=0 else 0 
    try:
        updates = get_list_or_404(Updates)[:5]
    except Http404:
        updates = ["No updates yet"]

    comments = Comment.objects.all()
    context = {'module_list':module_list,
               # 'completed_activity_list':completed_activity_list,
               #  'progress':progress,
                'updates':updates,
                'comments':comments}
    
    return render(request,'tt/index.djhtml',context)

def activity(request,url):
    activity = get_object_or_404(Aktivnost,url=url)

    return render(request,'tt/%s.djhtml' % url,{'activity':activity})


from django.contrib.auth import authenticate,login
from django.utils import timezone

def user_login(request):
    if request.method!='POST':
        # Ako nije post metoda
        return HttpResponse(reverse('tt:index'))
    try:
        #Ovde u principu ne bi trebalo
        #da ikada dodje, posto ce svejedno
        #onaj token napraviti problem ako
        # nije sa nase stranice,a ako je
        # sa nase onda mozemo osigurati
        username = request.POST['username']
        password = request.POST['password']
    except KeyError:
        return HttpResponseRedirect(reverse('tt:index'))
        
    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect(reverse('tt:index'))
        else:
            return HttpResponse("User inactive!")
    else:
        return HttpResponse("Bad login!")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('tt:index'))
    

def add_comment(request):
    user = request.user
    if user.is_authenticated():
        content = request.POST['comment']
        date = timezone.now()
        comment = Comment(user=user,content=content,date=date)
        comment.save()
        
    return HttpResponseRedirect(reverse('tt:index'))
    
def redirect_login(request):
    return render(request,'tt/login.djhtml')


    
    


    


