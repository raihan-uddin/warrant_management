from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView

from warrant.forms import WarrantCreateForm
from warrant.models import Warrant


# Warrant views start

class WarrantListTemplate(TemplateView):
    template_name = 'warrant/list.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['warrants'] = Warrant.objects.all()
        return data


class WarrantCreateTemplate(TemplateView):
    template_name = 'warrant/create.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = WarrantCreateForm(self.request.POST or None)  # instance= None
        return data

    def post(self, request, *args, **kwargs):
        print("POST DATA")
        form_warrant = WarrantCreateForm(data=request.POST)

        print(form_warrant.data)
        if form_warrant.is_valid():
            Warrant.objects.create(**form_warrant.cleaned_data)
            return self.render_to_response(
                context={'status': 'success', 'status_code': 200, 'message': 'Warrant created successfully!',
                         'form': WarrantCreateForm(), 'errors': None})
        else:
            print("NOT SAVED")
            return self.render_to_response(
                context={'status': 'error', 'status_code': 500, 'message': 'Please try again!', 'form': form_warrant,
                         'errors': form_warrant.errors})


class WarrantUpdateTemplate(UpdateView):
    model = Warrant
    fields = ('entry_date', 'issue_date', 'warrant_type', 'court_name', 'warrant_person_name_age',
              'warrant_person_father_name', 'district', 'thana', 'union', 'address', 'gr_cr_no', 'gr_cr_year',
              'case_file_station', 'concerned_police_unit', 'case_type_section', 'date_of_presentation_in_court',
              'court_process_no', 'court_given_other_info')
    template_name = 'warrant/update.html'
    context_object_name = 'warrant'
    success_url = '/warrant/list'


class WarrantFileUploadTemplate(TemplateView):
    template_name = 'warrant/file_upload.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['warrants'] = Warrant.objects.all()
        return data
