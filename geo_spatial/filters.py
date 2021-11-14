import django_filters
from .models import *


class DistrictFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    name_bn = django_filters.CharFilter(lookup_expr='icontains')
    code = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = District
        fields = '__all__'

