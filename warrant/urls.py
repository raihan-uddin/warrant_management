from user.views import UnionTemplate
from django.urls import path
from . import views

urlpatterns = [
    # warrant urls start
    path('warrant/', views.warrant_form, name='warrant_create'),
    path('warrant/<int:id>/', views.warrant_form, name='warrant_update'),
    path('warrant/delete/<int:id>/', views.warrant_delete, name='warrant_delete'),
    path('warrant/list/', views.warrant_list, name='warrant_list'),
    # warrant urls end
]
