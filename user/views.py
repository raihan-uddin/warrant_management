from user.models import CustomUser
from user.forms import UserForm
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView


# Create your views here.

# user views start

def user_list(request):
    data = {'user_list': CustomUser.objects.all()}
    return render(request, "user/list.html", data)


def user_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = UserForm()
        else:
            user = CustomUser.objects.get(pk=id)
            form = UserForm(instance=user)

        return render(request, "user/create.html", {'form': form, 'id': id})
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = CustomUser.objects.get(pk=id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('/user/list')


def user_delete(request, id):
    user = CustomUser.objects.get(pk=id)
    user.delete()
    return redirect('/user/list')
# user views end

class SampleTemplateView(TemplateView):
    template_name = 'user_list.html'


class DashboardTemplate(TemplateView):
    template_name = 'dashboard.html'

class UnionTemplate(TemplateView):
    template_name = 'union.html'