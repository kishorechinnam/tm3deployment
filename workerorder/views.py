from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from django.shortcuts import render
from .models import *
from .forms import *
from .models import WorkOrder
from django.urls import reverse_lazy


def WorkOrderListView(request):
    workorder = WorkOrder.objects.filter(user_id=request.user)
    return render(request, 'workorder_list.html', {'workorders': workorder})


def Workorder_new(request):
    if request.method == "POST":
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            workorder = form.save(commit=False)
            workorder.save()
            workorder = WorkOrder.objects.filter(promised_date=timezone.now())
            return render(request, 'workorder_list.html',
                          {'workorders': workorder})
    else:
        form = WorkOrderForm()
    return render(request, 'workorder_new.html', {'form': form})
