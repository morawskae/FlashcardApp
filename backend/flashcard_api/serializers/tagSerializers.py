from rest_framework import serializers
from ..models import Tag

class TagReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "title",
            "color"
        ]

class TagWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "title",
            "color"
        ]