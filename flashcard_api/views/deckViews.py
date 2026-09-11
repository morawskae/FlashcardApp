from rest_framework import viewsets
from ..models import Deck
from ..serializers import DeckWriteSerializer, DeckListSerializer, DeckDetaliedSerializer,FlashcardReadSerializer, FlashcardWriteSerializer
from .deckFlashcardActions import DeckFlashcardActions

class DeckViewSet(DeckFlashcardActions,viewsets.ModelViewSet):
    queryset = Deck.objects.all()

    def get_serializer_class(self):
        if self.action  =="list":
            return DeckListSerializer
        if self.action == "retrieve":
            return DeckDetaliedSerializer
        return DeckWriteSerializer
