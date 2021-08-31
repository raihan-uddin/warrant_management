from geo_spatial.models import Union, District
from geo_spatial.forms import UnionForm, DistrictCreateForm
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView


# union views start

class DistrictListTemplate(TemplateView):
    template_name = 'district/list.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['districts'] = District.objects.all()
        return data


class DistrictCreateTemplate(TemplateView):
    template_name = 'district/create.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = DistrictCreateForm(self.request.POST or None)  # instance= None
        return data

    def post(self, request, *args, **kwargs):
        form_district = DistrictCreateForm(data=request.POST)

        if form_district.is_valid():
            District.objects.create(**form_district.cleaned_data)
            return self.render_to_response(
                context={'status': 'success', 'status_code': 200, 'message': 'Warrant created successfully!',
                         'form': DistrictCreateForm(), 'errors': None})
        else:
            print("NOT SAVED")
            return self.render_to_response(
                context={'status': 'error', 'status_code': 500, 'message': 'Please try again!', 'form': form_district,
                         'errors': form_district.errors})


# district views end

# union views start

def union_list(request):
    data = {'union_list': Union.objects.all()}
    return render(request, "union/list.html", data)


def union_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = UnionForm()
        else:
            union = Union.objects.get(pk=id)
            form = UnionForm(instance=union)

        return render(request, "union/create.html", {'form': form, 'id': id})
    else:
        if id == 0:
            form = UnionForm(request.POST)
        else:
            union = Union.objects.get(pk=id)
            form = UnionForm(request.POST, instance=union)
        if form.is_valid():
            form.save()
        return redirect('/config/union/list')


def union_delete(request, id):
    union = Union.objects.get(pk=id)
    union.delete()
    return redirect('/config/union/list')
# union views end
