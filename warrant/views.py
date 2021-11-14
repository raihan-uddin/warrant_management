from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, UpdateView

from warrant.forms import WarrantCreateForm, WarrantFileModelForm
from warrant.models import Warrant, WarrantFile


# Warrant views start
@method_decorator(login_required, name='dispatch', )
class WarrantListTemplate(TemplateView):
    template_name = 'warrant/list.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['warrants'] = Warrant.objects.all()
        return data


@method_decorator(login_required, name='dispatch', )
class WarrantCreateTemplate(TemplateView):
    template_name = 'warrant/create.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = WarrantCreateForm(self.request.POST or None)  # instance= None
        data['warrant_file_form'] = WarrantFileModelForm(self.request.POST or None)
        return data

    def post(self, request, *args, **kwargs):
        form_warrant = WarrantCreateForm(data=request.POST, files=request.FILES)
        form_warrant_files = WarrantFileModelForm(data=request.POST, files=request.FILES)
        files = request.FILES.getlist('attachment')

        # print(form_warrant.data)
        if form_warrant.is_valid():
            warrant = Warrant.objects.create(**form_warrant.cleaned_data)
            if form_warrant_files.is_valid():
                for f in files:
                    file_instance = WarrantFile(attachment=f, warrant=warrant)
                    file_instance.save()
                    # WarrantFile.objects.create(warrant=warrant, **form_warrant_files.cleaned_data)
            return self.render_to_response(
                context={'status': 'success', 'status_code': 200, 'message': 'Warrant created successfully!',
                         'form': WarrantCreateForm(), 'warrant_file_form': WarrantFileModelForm(), 'errors': None})
        else:
            print("NOT SAVED")
            return self.render_to_response(
                context={'status': 'error', 'status_code': 500, 'message': 'Please try again!', 'form': form_warrant,
                         'warrant_file_form': form_warrant_files, 'errors': form_warrant.errors})


@method_decorator(login_required, name='dispatch', )
class WarrantUpdateTemplate(UpdateView):
    model = Warrant
    fields = ('entry_date', 'issue_date', 'warrant_type', 'court_name', 'warrant_person_name_age',
              'warrant_person_father_name', 'district', 'thana', 'union', 'address', 'gr_cr_no', 'gr_cr_year',
              'case_file_station', 'concerned_police_unit', 'case_type_section', 'date_of_presentation_in_court',
              'court_process_no', 'court_given_other_info')
    template_name = 'warrant/update.html'
    context_object_name = 'warrant'
    success_url = '/warrant/list'


@method_decorator(login_required, name='dispatch', )
class WarrantFileUploadTemplate(TemplateView):
    template_name = 'warrant/file_upload.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['warrants'] = Warrant.objects.all()
        return data
