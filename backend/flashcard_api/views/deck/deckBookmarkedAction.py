from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from ...utils import bookmarked_decks
from ...serializers import DeckListSerializer
from django.shortcuts import get_object_or_404
from ...models import Bookmark, Deck

class BookmarkedDecksGetAction(APIView):
        permission_classes=[
        IsAuthenticated]

        #get -> view bookmarked
        def get(self, request):
            decks = bookmarked_decks(request.user)
            serializer = DeckListSerializer(decks, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        
class BookmarkPostDelAction(APIView):
    permission_classes=[
        IsAuthenticated
    ]
    #post -> add deck to bookmarked
    #delete -> remove deck from bookmarked

    def post(self, request, pk=None):
        deck = get_object_or_404(Deck,is_public=True,pk=pk) #dont want to bookmark a deck user already owns
        if deck.owner == request.user:
            return Response({"detail": "You cannot bookmark your own deck."},status=status.HTTP_400_BAD_REQUEST)

        if Bookmark.objects.filter( deck=deck, user=request.user ).exists():
            return Response( {"detail": "Deck is already bookmarked."}, status=status.HTTP_400_BAD_REQUEST )

        Bookmark.objects.create_bookmark(deck,request.user)
        return Response(status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk=None):
        bookmark = get_object_or_404(Bookmark, deck_id=pk,user=request.user)
        bookmark.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)