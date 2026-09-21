from rest_framework import viewsets
from ..serializers import DeckWriteSerializer, DeckListSerializer, DeckDetaliedSerializer
from .deckFlashcardActions import DeckFlashcardActions

from rest_framework.permissions import IsAuthenticated
from ..utils import accessible_decks
class DeckViewSet(DeckFlashcardActions,viewsets.ModelViewSet):

    def get_queryset(self):
        return accessible_decks(self.request.user)

    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    
    def get_serializer_class(self):
        if self.action  =="list":
            return DeckListSerializer
        if self.action == "retrieve":
            return DeckDetaliedSerializer
        return DeckWriteSerializer
