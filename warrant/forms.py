from django import forms
from django.forms import fields

from warrant.models import Warrant


class WarrantForm(forms.ModelForm):
    class Meta:
        model = Warrant
        fields = '__all__'
        labels = {
            'gr_cr_no': 'GR CR No',
            'gr_cr_year': 'GR CR Year'
        }

    def __ini__(self, *args, **kwargs):
        super(WarrantForm, self).__init__(*args, **kwargs)
