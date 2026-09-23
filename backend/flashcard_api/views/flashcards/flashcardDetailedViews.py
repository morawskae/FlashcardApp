from ...serializers import FlashcardWriteSerializer, FlashcardReadSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ...utils import user_flashcards, accessible_flashcards

class FlashcardDetailedAPIView(RetrieveUpdateDestroyAPIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        if self.request.method=="GET":
            return accessible_flashcards(self.request.user)
        return user_flashcards(self.request.user)

    def get_serializer_class(self):
        if self.request.method=="GET":
            return FlashcardReadSerializer
        return FlashcardWriteSerializer