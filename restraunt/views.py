from django.shortcuts import render
from django.views import generic
from .models import Item
from django.urls import reverse_lazy
# Create your views here.
class Index(generic.ListView):
    template_name="index.html"
    context_object_name="item_list"

class Details(generic.DetailView):
    model = Item
    template_name="detail.html"
    
class Create(genereic.CreateView):
    model = Item
    template_name = "create.html"
    fields="__all__"

class Update(generic.UpdateView):
    model = Item
    template_name="create.html"
    fields="__all__"

class Delete(generic.DeleteView):
    model = Item
    template_name = "delete.html"
    success_url=reverse_lazy("restraunt:details")