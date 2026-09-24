from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='nature_index'),
    path('/new/biome', views.new_biome_view, name='new_biome'),
    path('/new/creature', views.new_creature_view, name='new_creature'),
]