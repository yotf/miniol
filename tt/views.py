from django.shortcuts import render


def index(request):
    module_list = Module.objects
    context = {'module_list':module_list}
    return render(request,'tt/index.djhtml',context)

    