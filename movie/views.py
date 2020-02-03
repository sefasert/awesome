from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Movie, MovieLink


class MovieList(ListView):
    model = Movie
    paginate_by = 1 #sayfada görüntülenen ürün



class MovieDetail(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):

        context = super(MovieDetail, self).get_context_data(**kwargs)

        context['links'] = MovieLink.objects.filter(movie=self.get_object()) #izleme link ekleme

        return context



   
   
   
    