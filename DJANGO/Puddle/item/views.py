from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Item 
from django.http import HttpResponse

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_item = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    template = loader.get_template('details.html')
    context = {
        'item':item,
        'related_item':related_item,       
    }
    return HttpResponse(template.render(context))
    # return render(request, 'details.html', { 'item':item })