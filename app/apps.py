from django.apps import AppConfig

from .models import *


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    
    class Meta:
        model = FashionContent, CelebrityContent, FinanceContent, PoliticsContent, SportsContent, ReceipesContent
        fields = ('url',)
