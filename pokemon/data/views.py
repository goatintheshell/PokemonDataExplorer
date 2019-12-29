from django.shortcuts import render
from data.models import Pokemon

# Create your views here.

def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    context = {
        'pokemon': pokemon
    }
    return render(request, 'pokemon_index.html', context)

def pokemon_detail(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    context = {
        'pokemon': pokemon
    }
    return render(request, 'pokemon_detail.html', context)