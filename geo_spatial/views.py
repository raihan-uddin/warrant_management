from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from geo_spatial.models import Union, District, Thana, PoliceUnit
from geo_spatial.forms import UnionForm, DistrictCreateForm, ThanaCreateForm, PoliceUnitCreateForm
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from .filters import District, DistrictFilter

import logging


# Get an instance of a logger
# logger = logging.getLogger(__name__)


@method_decorator(login_required, name='dispatch', )
class DistrictListTemplate(ListView):
    model = District
    template_name = 'district/list.html'
    context_object_name = 'districts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = DistrictFilter(self.request.GET, queryset)
        data['filters'] = filter
        # data['districts'] = District.objects.all()
        return data

    def get_queryset(self):
        logging.error('Something went wrong!')
        queryset = super().get_queryset()
        filter = DistrictFilter(self.request.GET, queryset)
        return filter.qs


@method_decorator(login_required, name='dispatch', )
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
                context={'status': 'success', 'status_code': 200, 'message': 'District created successfully!',
                         'form': DistrictCreateForm(), 'errors': None})
        else:
            print("NOT SAVED")
            return self.render_to_response(
                context={'status': 'error', 'status_code': 500, 'message': 'Please try again!', 'form': form_district,
                         'errors': form_district.errors})


# district views end


# Thana views start
@method_decorator(login_required, name='dispatch', )
class ThanaListTemplate(TemplateView):
    template_name = 'thana/list.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['thanas'] = Thana.objects.all()
        return data


@method_decorator(login_required, name='dispatch', )
class ThanaCreateTemplate(TemplateView):
    template_name = 'thana/create.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = ThanaCreateForm(self.request.POST or None)  # instance= None
        return data

    def post(self, request, *args, **kwargs):
        form_thana = ThanaCreateForm(data=request.POST)

        if form_thana.is_valid():
            Thana.objects.create(**form_thana.cleaned_data)
            return self.render_to_response(
                context={'status': 'success', 'status_code': 200, 'message': 'Thana created successfully!',
                         'form': ThanaCreateForm(), 'errors': None})
        else:
            print("NOT SAVED")
            return self.render_to_response(
                context={'status': 'error', 'status_code': 500, 'message': 'Please try again!', 'form': form_thana,
                         'errors': form_thana.errors})


# district views end

# union views start
@method_decorator(login_required, name='dispatch', )
def union_list(request):
    data = {'union_list': Union.objects.all()}
    return render(request, "union/list.html", data)


@method_decorator(login_required, name='dispatch', )
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


@method_decorator(login_required, name='dispatch', )
def union_delete(request, id):
    union = Union.objects.get(pk=id)
    union.delete()
    return redirect('/config/union/list')


# union views end

@method_decorator(login_required, name='dispatch', )
class PoliceUnitListTemplate(TemplateView):
    template_name = 'police-unit/list.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['police_units'] = PoliceUnit.objects.all()
        return data


@method_decorator(login_required, name='dispatch', )
class PoliceUnitCreateTemplate(TemplateView):
    template_name = 'police-unit/create.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = PoliceUnitCreateForm(self.request.POST or None)  # instance= None
        return data

    def post(self, request, *args, **kwargs):
        form_police_unit = PoliceUnitCreateForm(data=request.POST)

        if form_police_unit.is_valid():
            PoliceUnit.objects.create(**form_police_unit.cleaned_data)
            return self.render_to_response(
                context={'status': 'success', 'status_code': 200, 'message': 'Police Unit created successfully!',
                         'form': PoliceUnitCreateForm(), 'errors': None})
        else:
            print("NOT SAVED")
            return self.render_to_response(
                context={'status': 'error', 'status_code': 500, 'message': 'Please try again!',
                         'form': form_police_unit,
                         'errors': form_police_unit.errors})


# district views end


def load_cities(request):
    district_id = request.GET.get('district')
    if int(district_id.strip() or 0) > 0:
        districts = Thana.objects.filter(district_id=district_id).order_by('name')
    else:
        districts = None
    return render(request, 'thana/include/thana_dropdown_list_options.html', {'districts': districts})


def load_union(request):
    thana_id = request.GET.get('thana')
    if int(thana_id.strip() or 0) > 0:
        unions = Union.objects.filter(thana_id=thana_id).order_by('name')
    else:
        unions = None
    return render(request, 'union/include/union_dropdown_list_options.html', {'unions': unions})
