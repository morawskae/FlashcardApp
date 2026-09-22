from rest_framework import serializers
from ..models import Deck


class DeckListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = "owner.username")
    class Meta:
        model=Deck
        fields = [
            "id",
            "title",
            "owner"
        ]

class DeckDetaliedSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = "owner.username")
    class Meta:
        model = Deck 
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "is_public",
            "owner"
        ]

class DeckWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = [
            "title",
            "description",
            "is_public"
        ]

