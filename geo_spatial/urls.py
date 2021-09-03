from user.views import UnionTemplate
from django.urls import path
from . import views
from .views import DistrictCreateTemplate, DistrictListTemplate, ThanaListTemplate, ThanaCreateTemplate, \
    PoliceUnitCreateTemplate, PoliceUnitListTemplate

urlpatterns = [
    # district urls start
    path('district/create', DistrictCreateTemplate.as_view(), name='district_create'),
    path('district/list/', DistrictListTemplate.as_view(), name='district_list'),
    # district urls end

    # thana urls start
    path('thana/create', ThanaCreateTemplate.as_view(), name='thana_create'),
    path('thana/list/', ThanaListTemplate.as_view(), name='thana_list'),
    # thana urls end

    # thana urls start
    path('police-unit/create', PoliceUnitCreateTemplate.as_view(), name='police_unit_create'),
    path('police-unit/list/', PoliceUnitListTemplate.as_view(), name='police_unit_list'),
    # thana urls end

    # union urls start
    path('union/', views.union_form, name='union_create'),
    path('union/<int:id>/', views.union_form, name='union_update'),
    path('union/delete/<int:id>/', views.union_delete, name='union_delete'),
    path('union/list/', views.union_list, name='union_list'),
    # union urls end


    path('ajax/load-thanas/', views.load_cities, name='ajax_load_thana'),
    path('ajax/load-union/', views.load_union, name='ajax_load_union')
]
