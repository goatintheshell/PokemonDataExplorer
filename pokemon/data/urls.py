from django.urls import path
from . import views

urlpatterns = [
    path("", views.pokemon_index, name="pokemon_index"),
    path("<int:pk>/", views.pokemon_detail, name="pokemon_detail"),
    
]