from rest_framework import viewsets
from ..serializers import DeckWriteSerializer, DeckListSerializer, DeckDetaliedSerializer
from .deckFlashcardActions import DeckFlashcardActions

from rest_framework.permissions import IsAuthenticated
from ..utils import user_decks, accessible_decks
from django.shortcuts import get_object_or_404
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
    
    def get_serializer_class(self):
        if self.action  =="list":
            return DeckListSerializer
        if self.action == "retrieve":
            return DeckDetaliedSerializer
        return DeckWriteSerializer
