from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import fields, DateField, IntegerField, CharField, ChoiceField
from django.utils.safestring import mark_safe

from warrant.models import Warrant


class WarrantCreateForm(forms.ModelForm):
    class Meta:
        model = Warrant
        fields = ('entry_date', 'issue_date', 'warrant_type', 'court_name', 'warrant_person_name_age',
                  'warrant_person_father_name', 'district', 'thana', 'union', 'address', 'gr_cr_no', 'gr_cr_year',
                  'case_file_station', 'concerned_police_unit', 'case_type_section', 'date_of_presentation_in_court',
                  'court_process_no', 'court_given_other_info')
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4, 'cols': 5}),
            'court_given_other_info': forms.Textarea(attrs={'rows': 4, 'cols': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['court_given_other_info'].required = False
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
