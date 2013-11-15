from django.shortcuts import render
from tt.models import Module


def index(request):
    module_list = Module.objects.all()
    print type(Module.objects)
    context = {'module_list':module_list}
    return render(request,'tt/index.djhtml',context)

    