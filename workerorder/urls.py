from django.urls import path
from . import views

urlpatterns = [
    path('workorder_list', views.WorkOrderListView, name='workorder_list'),
    path('workorder_new/', views.Workorder_new, name='workorder_new'),
]
