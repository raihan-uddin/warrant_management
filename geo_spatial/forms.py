from django import forms
from django.forms import fields
from .models import Union

class UnionForm(forms.ModelForm):
    
    class Meta:
        model= Union
        fields = '__all__'
        labels = {
            'name_bn' : 'Name Bangla'
        }

    
    def __ini__(self, *args, **kwargs):
        super(UnionForm,self).__init__(*args, **kwargs)
        self.fields['thana'].empty_label = "Select"