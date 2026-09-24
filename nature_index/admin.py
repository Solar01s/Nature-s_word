from django.contrib import admin
from .models import Biome, Creature

class CreatureInline(admin.TabularInline):
    model = Creature.biomes.through
    extra = 1
    autocomplete_fields = ['creature']

@admin.register(Biome)
class BiomeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [CreatureInline]


@admin.register(Creature)
class CreatureAdmin(admin.ModelAdmin):
    search_fields = ['name']