from django import forms
from django.forms import fields

from warrant.models import Warrant


class WarrantForm(forms.ModelForm):
    class Meta:
        model = Warrant
        fields = '__all__'
        labels = {
            # 'name_bn': 'Name Bangla'
        }

    def __ini__(self, *args, **kwargs):
        super(WarrantForm, self).__init__(*args, **kwargs)
        self.fields['thana'].empty_label = "Select"
