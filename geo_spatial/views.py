from geo_spatial.models import Union
from geo_spatial.forms import UnionForm
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

# Create your views here.

# union views start

def union_list(request):
    data = {'union_list' : Union.objects.all()}
    return render (request,"union/list.html",data)

def union_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = UnionForm()
        else:
            union = Union.objects.get(pk=id)
            form = UnionForm(instance=union)

        return render (request,"union/create.html",{'form': form,'id': id})
    else:
        if id == 0:
            form = UnionForm(request.POST)
        else:
            union = Union.objects.get(pk=id)
            form = UnionForm(request.POST,instance=union)
        if form.is_valid():
            form.save()
        return redirect('/config/union/list')

def union_delete(request,id):
    union = Union.objects.get(pk=id)
    union.delete()
    return redirect('/config/union/list')
# union views end