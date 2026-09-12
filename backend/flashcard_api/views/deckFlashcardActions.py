from ..models import Flashcard
from ..serializers import ( FlashcardWriteSerializer, FlashcardReadSerializer)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
class DeckFlashcardActions():
    
    @action(detail = True, methods=["GET","POST"])
    def flashcards(self, request,pk=None):
        deck = self.get_object()
        if( request.method=="GET"):
            flashcards = Flashcard.objects.filter(deck = deck)
            serializer = FlashcardReadSerializer(flashcards, many=True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        if(request.method =="POST"):
            serializer = FlashcardWriteSerializer(data=request.data)
            if serializer.is_valid():
                flashcard = serializer.save(deck=deck)
                read_serializer = FlashcardReadSerializer(flashcard)
                return Response(read_serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)