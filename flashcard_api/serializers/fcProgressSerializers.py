from rest_framework import serializers
from ..models import FcProgress


#zastanow sie czy to wgl jest potrzebne
class FcProgressReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FcProgress
        fields = [
            "id",
            "flashcard",
            "due_at",
            "last_reviewed_at",
            "successful_repetitions",
            "ease_factor",
            "interval"
        ]


