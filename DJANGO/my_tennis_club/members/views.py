from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Member
# Create your views here.

def members(request):
    mymembers = Member.objects.all().values()
    return render(request, 'allmembers.html', {'mymembers':mymembers})
    # template = loader.get_template('myFirst.html')
    # return HttpResponse(template.render())

def details(request, id):
    mymember = Member.objects.get(id=id)
    # return render(request, 'details.html', {'mymember':mymember})
    template = loader.get_template('details.html')
    context = {'mymember':mymember}
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())