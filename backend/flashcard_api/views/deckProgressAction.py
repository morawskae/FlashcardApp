from ..models import Flashcard
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from serializers import FlashcardReadSerializer

class DeckProgressAction():
    @action(detail=True, methods=["Get"],url_path="flashcards/due")
    def repeat(self, request,pk=None):
        deck = self.get_object()
        now = timezone.now()

        flashcards = Flashcard.objects.filter(deck=deck, progress__due_at__lte=now)
        serializer = FlashcardReadSerializer(flashcards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)