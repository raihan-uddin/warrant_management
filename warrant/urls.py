from user.views import UnionTemplate
from django.urls import path
from . import views
from .views import WarrantCreateTemplate, WarrantListTemplate, WarrantFileUploadTemplate

urlpatterns = [
    # warrant urls start
    # path('', views.warrant_form, name='warrant_create'),
    # path('delete/<int:id>/', views.warrant_delete, name='warrant_delete'),
    # warrant urls end

    path('create', WarrantCreateTemplate.as_view(), name='warrant_create'),
    path('list/', WarrantListTemplate.as_view(), name='warrant_list'),
    path('<int:id>/', views.WarrantUpdateTemplate, name='warrant_update'),
]
