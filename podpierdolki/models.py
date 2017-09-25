from django.db import models


class Brudas(models.Model):
    nazwa = models.CharField(max_length=256)

    def __str__(self):
        return self.nazwa


class Donos(models.Model):
    tytul = models.CharField(max_length=256)
    tresc = models.TextField()

    obsmarowany = models.ForeignKey(Brudas)

    def __str__(self):
        return self.tytul
