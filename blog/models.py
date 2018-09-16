from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
class Artikelnummer(models.Model):
    artikelnummer = models.CharField(max_length=8 , primary_key=True)
    artikelbezeichnung = models.CharField(max_length = 100 )

    def __str__(self):
        return self.artikelbezeichnung

class Rezeptur(models.Model):
    rezeptnummer = models.CharField(max_length=10, primary_key=True)
    rezeptbezeichnung = models.CharField(max_length=100)

    def __str__(self):
        return self.rezeptbezeichnung
