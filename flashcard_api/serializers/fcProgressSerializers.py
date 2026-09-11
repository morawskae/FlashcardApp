from rest_framework import serializers
from ..models import Progress


class ProgressReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = [
            "id",
            "flashcard",
            "due_at",
            "last_reviewed_at",
            "successful_repetitions",
            "ease_factor",
            "interval"
        ]


