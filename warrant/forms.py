from django import forms
from django.forms import ClearableFileInput

from geo_spatial.models import Thana, Union
from warrant.models import Warrant, WarrantFile


class WarrantCreateForm(forms.ModelForm):
    class Meta:
        model = Warrant
        fields = ('entry_date', 'issue_date', 'warrant_type', 'court_name', 'warrant_person_name_age',
                  'warrant_person_father_name', 'district', 'thana', 'union', 'address', 'gr_cr_no', 'gr_cr_year',
                  'case_file_station', 'concerned_police_unit', 'case_type_section', 'date_of_presentation_in_court',
                  'court_process_no', 'court_given_other_info', 'picture')
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4, 'cols': 5}),
            'court_given_other_info': forms.Textarea(attrs={'rows': 4, 'cols': 5}),
            # 'picture': forms.FileField(label='Select a file',
            #                            help_text='max. 42 megabytes')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['thana'].queryset = Thana.objects.none()
        self.fields['union'].queryset = Union.objects.none()
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['thana'].queryset = Thana.objects.filter(district_id=district_id).order_by('name')
            except(ValueError, TypeError):
                pass  # invalid input from the client;
        elif self.instance.pk:
            self.fields['thana'].queryset = self.instance.thana_set.order_by('name')

        if 'thana' in self.data:
            try:
                thana_id = int(self.data.get('thana'))
                self.fields['union'].queryset = Union.objects.filter(thana_id=thana_id).order_by('name')
            except(ValueError, TypeError):
                pass  # invalid input from the client;
        elif self.instance.pk:
            self.fields['union'].queryset = self.instance.union_set.order_by('name')


class WarrantFileModelForm(forms.ModelForm):
    class Meta:
        model = WarrantFile
        fields = ['attachment']
        widgets = {
            'attachment': ClearableFileInput(attrs={'multiple': True}),
        }  # widget is important to upload multiple files

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
