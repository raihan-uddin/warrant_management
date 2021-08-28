from user.views import UnionTemplate
from django.urls import path
from . import views

urlpatterns = [
    # union urls start
    path('union/', views.union_form, name='union_create'),
    path('union/<int:id>/', views.union_form, name='union_update'),
    path('union/delete/<int:id>/', views.union_delete, name='union_delete'),
    path('union/list/', views.union_list, name='union_list'),
    # union urls end
]
