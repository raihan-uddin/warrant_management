import django_filters
from .models import *


class DistrictFilter(django_filters.FilterSet):
    class Meta:
        model = District
        fields = '__all__'
