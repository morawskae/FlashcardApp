from ..models import Flashcard, Progress
from ..serializers import ( FlashcardWriteSerializer, FlashcardReadSerializer)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from ..utils import accessible_decks

class DeckFlashcardActions():

    permission_classes = [
        IsAuthenticated,
        
    ]
    
    @action(detail = True, methods=["GET","POST"])
    def flashcards(self, request,pk=None):
        deck = get_object_or_404(accessible_decks(request.user),pk=pk)

        if( request.method=="GET"):
            flashcards = Flashcard.objects.filter(deck = deck)
            serializer = FlashcardReadSerializer(flashcards, many=True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        if(request.method =="POST"):
            serializer = FlashcardWriteSerializer(data=request.data)
            if serializer.is_valid():
                flashcard = serializer.save(deck=deck)
                #Progress.objects.create_progress(flashcard = flashcard, user=request.user)
                read_serializer = FlashcardReadSerializer(flashcard)
                return Response(read_serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)