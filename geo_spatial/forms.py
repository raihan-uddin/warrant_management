from django import forms
from django.forms import fields
from .models import Union, District, Thana, PoliceUnit


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


class ThanaCreateForm(forms.ModelForm):
    class Meta:
        model = Thana
        fields = ('district', 'name', 'name_bn', 'code')

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


class PoliceUnitCreateForm(forms.ModelForm):
    class Meta:
        model = PoliceUnit
        fields = ('name', 'name_bn', 'contact_person', 'contact_no', 'email', 'remarks')

        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 4, 'cols': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
