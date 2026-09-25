from django.shortcuts import render, redirect
from .models import Biome, Creature
from django.shortcuts import get_object_or_404
from .forms import BiomeForm, CreatureForm
import random

def index_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        biomes = Biome.objects.filter(name__icontains=query).prefetch_related('related_biomes', 'creatures')
        creatures = Creature.objects.filter(name__icontains=query).prefetch_related('biomes', 'related_creatures')
    else:
        biomes = Biome.objects.all().prefetch_related('related_biomes', 'creatures')
        creatures = Creature.objects.all().prefetch_related('biomes', 'related_creatures')
    mixed = list(biomes) + list(creatures)
    random.shuffle(mixed)
    return render(request, 'nature_index/index.html', {'items': mixed})

def new_creature_view(request):
    if request.method == 'POST':
        form = CreatureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nature_index')
        else:
            print("ОШИБКИ СОЗДАНИЯ ФОРМЫ СОЗДАНИЯ: ", form.errors)
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
            print("ОШИБКИ СОЗДАНИЯ ФОРМЫ БИОМА: ", form.errors)
    else:
        form = BiomeForm()
    return render(request, 'nature_index/new_biome.html', {'form': form})

def biome_view(request, biome_id):
    biome = get_object_or_404(Biome, pk=biome_id)
    return render(request, 'nature_index/biome.html', {'biome': biome})

def creature_view(request, creature_id):
    creature = get_object_or_404(Creature, pk=creature_id)
    return render(request, 'nature_index/creature.html', {'creature': creature})
