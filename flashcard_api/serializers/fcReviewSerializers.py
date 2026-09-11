from rest_framework import serializers
from ..models import FcReview, Rating

class FcReviewReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FcReview
        fields = [
            "id",
            "flashcard",
            "reviewed_at",
            "rating"
        ]

#for adding reviews
class ReviewSubmitSerializer(serializers.ModelSerializer):
    model = FcReview
    rating = serializers.ChoiceField(choices=Rating.choices)