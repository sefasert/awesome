from django.db import models

# Create your models here.

CATEGORY_CHOICES = {

    ('A', 'ACTION'),
    ('D', 'DRAMA'),
    ('C', 'COMEDY'),
    ('R', 'ROMANCE'),

}

LANGUAGE_CHOCES = {

    ('EN', 'ENGLISH'),
    ('GR', 'GERMAN'),
}

STATUS_CHOCES = {

    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED'),
}


class Movie(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOCES)
    status = models.CharField(max_length=20, choices=STATUS_CHOCES)
    year_of_production = models.DateField()


    def __str__(self):
        return self.title


LINK_CHOCES = {

    ('D', 'DOWNLOAD LINK'),
    ('W', 'WATCH LINK')
}


class MovieLink(models.Model):

    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=LINK_CHOCES)
    link = models.URLField()

    def __str__(self):
        return str (self.movie)
    

          

