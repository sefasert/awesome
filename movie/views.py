from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Movie


class MovieList(ListView):
    model = Movie
    paginate_by = 1 #sayfada görüntülenen ürün
   # context_object_name = ''
   # template_name=''


class MovieDetail(DetailView):
    model = Movie
   # template_name=''    