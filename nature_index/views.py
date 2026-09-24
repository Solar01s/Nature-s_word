from django.shortcuts import render, redirect
from .models import Biome, Creature
from django.shortcuts import get_object_or_404
from .forms import BiomeForm, CreatureForm
import random

def index_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        biomes = Biome.objects.filter(name__icontains=query)
        creatures = Creature.objects.filter(name__icontains=query)
    else:
        biomes = Biome.objects.all()
        creatures = Creature.objects.all()
    mixed = list(biomes) + list(creatures)
    items = random.shuffle(mixed)
    return render(request, 'nature_index/index.html', {'items': items})

def new_creature_view(request):
    if request.method == 'POST':
        form = CreatureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nature_index')
    else:
        form = CreatureForm()
    return render(request, 'nature_index/new_creature.html', {'form': form})


def new_biome_view(request):
    if request.method == 'POST':
        form = BiomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nature_index')
    else:
        form = BiomeForm()
    return render(request, 'nature_index/new_biome.html', {'form': form})

def biome_view(request, biome_id):
    Biomes = get_object_or_404(Biome, pk=biome_id)
    return render(request, 'nature_index/biome.html', {'Biomes': Biomes})

def creature_view(request, creature_id):
    Creatures = get_object_or_404(Creature, pk=creature_id)
    return render(request, 'nature_index/creature.html', {'Creatures': Creatures})
