from user.views import UnionTemplate
from django.urls import path
from . import views
from .views import DistrictCreateTemplate, DistrictListTemplate

urlpatterns = [
    # district urls start
    path('create', DistrictCreateTemplate.as_view(), name='district_create'),
    path('list/', DistrictListTemplate.as_view(), name='district_list'),
    # district urls end

    # union urls start
    path('union/', views.union_form, name='union_create'),
    path('union/<int:id>/', views.union_form, name='union_update'),
    path('union/delete/<int:id>/', views.union_delete, name='union_delete'),
    path('union/list/', views.union_list, name='union_list'),
    # union urls end
]
