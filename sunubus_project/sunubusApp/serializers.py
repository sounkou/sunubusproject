from rest_framework import serializers
from .models import Heroes
from .models import Ligne

class HeroesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Heroes
        fields = ('idHero', 'nom', 'prenom', 'email','address','password', )

class LigneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ligne
        fields = ('idLigne', 'compagnie',)  