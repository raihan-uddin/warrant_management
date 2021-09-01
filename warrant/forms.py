from django import forms
from warrant.models import Warrant


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
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

