from rest_framework import serializers
from ..models import Review, Rating

class ReviewReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "flashcard",
            "reviewed_at",
            "rating"
        ]

#for adding reviews
class ReviewSubmitSerializer(serializers.ModelSerializer):
    model = Review
    rating = serializers.ChoiceField(choices=Rating.choices)