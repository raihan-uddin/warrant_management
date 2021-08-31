from django import forms
from django.forms import fields
from .models import Union, District


class DistrictCreateForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ('name', 'name_bn', 'code')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UnionForm(forms.ModelForm):
    class Meta:
        model = Union
        fields = '__all__'
        labels = {
            'name_bn': 'Name Bangla'
        }

    def __ini__(self, *args, **kwargs):
        super(UnionForm, self).__init__(*args, **kwargs)
        self.fields['thana'].empty_label = "Select"
