from django import forms
from .models import Biome, Creature

class BiomeForm(forms.ModelForm):

    creatures = forms.ModelMultipleChoiceField(
        queryset=Creature.objects.all(),
        required=False,)

    class Meta:
        model = Biome
        fields = ['name', 'description', 'image', 'creatures', 'related_biomes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Ocean'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe this Biome...'}),
            'image': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'image url e.g. https"//biome_photos.com/1234/'}),
            'related_biomes': forms.CheckboxSelectMultiple(),
            'creatures': forms.CheckboxSelectMultiple(),
        }

    def save(self, commit=True):
        instance = super().save(commit=commit)
        if commit:
            instance.creatures.set(self.cleaned_data['creatures'])
        return instance

class CreatureForm(forms.ModelForm):
    class Meta:
        model = Creature
        fields = ['name', 'description', 'image', 'biomes', 'related_creatures']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Tiger'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe this Creature...'}),
            'image': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'image url e.g. https"//creature_photos.com/1234/'}),
            'biomes': forms.CheckboxSelectMultiple(),
            'related_creatures': forms.CheckboxSelectMultiple(),

        }
