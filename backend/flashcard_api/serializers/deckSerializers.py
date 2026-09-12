from rest_framework import serializers
from ..models import Deck


class DeckListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Deck
        fields = [
            "id",
            "title"
        ]

class DeckDetaliedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck 
        fields = [
            "id",
            "title",
            "description",
            "created_at"
        ]

class DeckWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = [
            "title",
            "description"
        ]

