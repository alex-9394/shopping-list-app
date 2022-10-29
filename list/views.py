from django.urls import reverse_lazy
from .models import Item
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'home.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = context['items'].filter(user=self.request.user)
        return context


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'item_detail.html'


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = 'item_new.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = 'item_edit.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('home')


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'item_delete.html'
    context_object_name = 'item'
    success_url = reverse_lazy('home')