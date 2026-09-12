from ..models import Flashcard, Deck
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from ..serializers import FlashcardReadSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class DeckProgressAction(APIView):
    #@action(detail=True, methods=["Get"],url_path="flashcards/due")
    def get(self, request,pk=None):
        deck = get_object_or_404(Deck, pk=pk)
        now = timezone.now()

        flashcards = Flashcard.objects.filter(deck=deck, progress__due_at__lte=now)
        serializer = FlashcardReadSerializer(flashcards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)