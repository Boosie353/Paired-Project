from django.db import models


# Create your models here.

class FashionContent(models.Model):
    headline = models.CharField(max_length=300)
    img = models.URLField(null=True, blank=True)
    url = models.TextField()
    def __str__(self):
        return self.headline

class CelebrityContent(models.Model):
    headline = models.CharField(max_length=300)
    img = models.URLField(null=True, blank=True)
    url = models.TextField()
    def __str__(self):
        return self.headline

class FinanceContent(models.Model):
    headline = models.CharField(max_length=300)
    img = models.URLField(null=True, blank=True)
    url = models.TextField()
    def __str__(self):
        return self.headline

class PoliticsContent(models.Model):
    headline = models.CharField(max_length=300)
    img = models.URLField(null=True, blank=True)
    url = models.TextField()
    def __str__(self):
        return self.headline

class SportsContent(models.Model):
    headline = models.CharField(max_length=300)
    img = models.URLField(null=True, blank=True)
    url = models.TextField()
    def __str__(self):
        return self.headline

class ReceipesContent(models.Model):
    headline = models.CharField(max_length=300)
    img = models.URLField(null=True, blank=True)
    url = models.TextField()
    def __str__(self):
        return self.headline
