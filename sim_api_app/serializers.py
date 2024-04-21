from rest_framework import serializers
from .models import SimsPack, Trait

class SimsPackSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SimsPack
        fields = ('pk', 'name', 'icon', 'type')

class TraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trait
        fields = ('pk', 'name', 'icon', 'description', 'type', 'ambition_type', 'trait_subtype', 'effect', 'pack')