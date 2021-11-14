# from user.views import UnionTemplate
from django.urls import path
from . import views

urlpatterns = [
    # user urls start
    path('create/', views.user_form, name='user_create'),
    path('<int:id>/', views.user_form, name='user_update'),
    path('delete/<int:id>/', views.user_delete, name='user_delete'),
    path('list/', views.user_list, name='user_list'),
    # user urls end
]
