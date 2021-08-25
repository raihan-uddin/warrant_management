from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class SampleTemplateView(TemplateView):
    template_name = 'user_list.html'
