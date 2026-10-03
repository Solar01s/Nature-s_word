from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='nature_index'),
    path('new/biome/', views.new_biome_view, name='new_biome'),
    path('new/creature/', views.new_creature_view, name='new_creature'),
    path('edit_biome/<int:pk>/',views.edit_biome_view, name='edit_biome'),
    path('edit_creature/<int:pk>/',views.edit_creature_view, name='edit_creature'),
    
    path('biome/<int:pk>/', views.biome_view, name='biome'),
    path('creature/<int:pk>/', views.creature_view, name='creature'),
]
