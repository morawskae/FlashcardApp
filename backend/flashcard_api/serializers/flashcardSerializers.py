from rest_framework import serializers
from ..models import Flashcard


#deck will be determined based on the deck endpoint
class FlashcardReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = [
            "id",
            "front_side",
            "back_side",
            "deck"
        ]

class FlashcardWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = [
            "front_side",
            "back_side",
        ]

