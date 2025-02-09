from django.shortcuts import render
from .models import Films
from django.urls import reverse_lazy
from django.views.generic import ListView

class FilmsListView(ListView):
    model = Films
    template_name = 'films_list.html'
    context_object_name = 'films'
    paginate_by = 1
