from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from . models import table
def index(request):
    return HttpResponse("Hello World")
def html(request):
   template=loader.get_template('port.html')
   return HttpResponse(template.render())
# Create your views here.
def index2(request):
    mymembers=table.objects.all().values()
    output=" "
    for x in mymembers:
        output+=x["first_name"]+x["last_name"]
    return HttpResponse(output)
def table1(request):
    mymembers=table.objects.all().values()
    template=loader.get_template('table.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))
def add(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render({}, request))
def addrecord(request):
    x=request.POST['first']
    y=request.POST['last']
    member=table(first_name=x,last_name=y)
    member.save()
    return HttpResponseRedirect(reverse("table1"))