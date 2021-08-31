from django import forms
from django.forms import fields
from .models import CustomUser


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
