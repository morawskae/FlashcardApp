from ..models import Flashcard
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from ..serializers import FlashcardReadSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from ..utils import user_decks

class DeckProgressAction(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    def get(self, request,pk=None):
        deck = get_object_or_404(user_decks(request.user), pk=pk) #include bookmarked decks in the future
        now = timezone.now()

        flashcards = Flashcard.objects.filter(deck=deck, progress__due_at__lte=now)
        serializer = FlashcardReadSerializer(flashcards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)