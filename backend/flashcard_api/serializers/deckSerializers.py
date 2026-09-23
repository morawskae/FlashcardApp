from rest_framework import serializers
from ..models import Deck
from .tagSerializers import TagReadSerializer


class DeckListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = "owner.username")
    tags = TagReadSerializer(many=True, read_only=True)
    class Meta:
        model=Deck
        fields = [
            "id",
            "title",
            "owner",
            "tags"
        ]

class DeckDetaliedSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = "owner.username")
    tags = TagReadSerializer(many=True, read_only=True)
    class Meta:
        model = Deck 
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "is_public",
            "owner",
            "tags"
        ]

class DeckWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = [
            "title",
            "description",
            "is_public"
        ]

