from rest_framework import viewsets
from ..models import Deck
from ..serializers import DeckWriteSerializer, DeckListSerializer, DeckDetaliedSerializer

class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()

    def get_serializer_class(self):
        if self.action  =="list":
            return DeckListSerializer
        if self.action == "retrieve":
            return DeckDetaliedSerializer
        return DeckWriteSerializer