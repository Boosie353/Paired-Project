from django.contrib import admin
from django.contrib import sites
from .models import FashionContent, CelebrityContent, FinanceContent, PoliticsContent, SportsContent, ReceipesContent


# Register your models here.
admin.site.register(FashionContent)
admin.site.register(CelebrityContent)
admin.site.register(FinanceContent)
admin.site.register(PoliticsContent)
admin.site.register(SportsContent)
admin.site.register(ReceipesContent)