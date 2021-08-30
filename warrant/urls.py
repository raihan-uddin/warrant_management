from user.views import UnionTemplate
from django.urls import path
from . import views

urlpatterns = [
    # warrant urls start
    path('', views.warrant_form, name='warrant_create'),
    path('<int:id>/', views.warrant_form, name='warrant_update'),
    path('delete/<int:id>/', views.warrant_delete, name='warrant_delete'),
    path('list/', views.warrant_list, name='warrant_list'),
    # warrant urls end
]
