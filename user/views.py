from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from user.models import CustomUser
from user.forms import UserForm
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView


# Create your views here.

# user views start
@method_decorator(login_required, name='dispatch', )
def user_list(request):
    data = {'user_list': CustomUser.objects.all()}
    return render(request, "user/list.html", data)

@method_decorator(login_required, name='dispatch', )
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

@method_decorator(login_required, name='dispatch', )
def user_delete(request, id):
    user = CustomUser.objects.get(pk=id)
    user.delete()
    return redirect('/user/list')


# user views end
@method_decorator(login_required, name='dispatch', )
class SampleTemplateView(TemplateView):
    template_name = 'user_list.html'


@method_decorator(login_required, name='dispatch', )
class DashboardTemplate(TemplateView):
    template_name = 'dashboard.html'

@method_decorator(login_required, name='dispatch', )
class UnionTemplate(TemplateView):
    template_name = 'union.html'
