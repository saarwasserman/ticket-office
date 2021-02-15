from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class meta:
        verbose_name_plural = 'categories'


class Venue(models.Model):

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return '%s - %s, %s' % (self.name, self.city, self.country)


class Event(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    artist = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.CharField(max_length=200)
    image_url = models.CharField(max_length=150)
    category = models.ForeignKey('Category', on_delete=models.RESTRICT)
    venue = models.ForeignKey('Venue', on_delete=models.RESTRICT)

    def __str__(self):
        return "%s, %s - %s" % (self.name, self.artist, self.venue)