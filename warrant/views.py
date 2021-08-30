from django.shortcuts import render, redirect

from warrant.forms import WarrantForm
from warrant.models import Warrant


# Warrant views start

def warrant_list(request):
    data = {'warrant_list': Warrant.objects.all()}
    return render(request, "warrant/list.html", data)


def warrant_form(request, id=0):
    print('ex')
    if request.method == 'GET':
        if id == 0:
            form = WarrantForm()
        else:
            warrant = Warrant.objects.get(pk=id)
            form = WarrantForm(instance=warrant)

        return render(request, "warrant/create.html", {'form': form, 'id': id})
    else:
        if id == 0:
            form = WarrantForm(request.POST)
        else:
            union = Warrant.objects.get(pk=id)
            form = WarrantForm(request.POST, instance=union)
        if form.is_valid():
            form.save()
        return redirect('/warrant/warrant/list')


def warrant_delete(request, id):
    warrant = Warrant.objects.get(pk=id)
    warrant.delete()
    return redirect('/warrant/warrant/list')
# warrant views end
