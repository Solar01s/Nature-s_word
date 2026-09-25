from django.db import models

class Biome(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=20_000)
    image = models.URLField(max_length=1500)
    climate = models.CharField(max_length=500)

    related_biomes = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.name

class Creature(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=20_000)
    image = models.URLField(max_length=500)

    biomes = models.ManyToManyField(Biome, related_name='creatures')
    created_at = models.DateTimeField(auto_now_add=True)
    related_creatures = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.name
