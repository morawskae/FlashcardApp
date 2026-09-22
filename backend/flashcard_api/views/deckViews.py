from rest_framework import viewsets
from ..serializers import DeckWriteSerializer, DeckListSerializer, DeckDetaliedSerializer
from .deckFlashcardActions import DeckFlashcardActions
from rest_framework.permissions import IsAuthenticated
from ..utils import user_decks, accessible_decks, has_bookmarks
from rest_framework.response import Response
from rest_framework import status

class DeckViewSet(DeckFlashcardActions,viewsets.ModelViewSet):

    def get_queryset(self):
        if self.action in ["retrieve"]:
            return accessible_decks(self.request.user)
        return user_decks(self.request.user)

    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def destroy(self, request, *args, **kwargs):
        deck = self.get_object()
        if(has_bookmarks(deck)):
            return Response({"detail":"Cannot delete deck with bookmarks"},status=status.HTTP_400_BAD_REQUEST)
    
    def get_serializer_class(self):
        if self.action  =="list":
            return DeckListSerializer
        if self.action == "retrieve":
            return DeckDetaliedSerializer
        return DeckWriteSerializer
