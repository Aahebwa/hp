from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import Item 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_item = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    template = loader.get_template('details.html')
    context = {
        'item':item,
        'related_item':related_item,       
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'details.html', { 'item':item })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    template = loader.get_template('form.html')
    context = {'form':form}
    return HttpResponse(template.render(context, request))


def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    
    return redirect('dashboard:index')