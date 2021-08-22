
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.scraping, name='scrap' ),
     path('allnews',views.news, name='scrapnews' ),
]