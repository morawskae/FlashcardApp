from rest_framework.response import Response
from rest_framework import status
from ..models import Flashcard
from ..serializers import FlashcardWriteSerializer, FlashcardReadSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class FlashcardDetailedAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Flashcard.objects.all()

    def get_serializer_class(self):
        if self.request.method=="GET":
            return FlashcardReadSerializer
        return FlashcardWriteSerializer