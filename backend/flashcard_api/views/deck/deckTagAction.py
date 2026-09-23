from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from ...utils import accessible_tags, user_decks, accessible_decks
from rest_framework.response import Response
from rest_framework import status
from ...serializers import TagReadSerializer

class DeckTagPostDelAction(APIView):
    permission_classes=[
        IsAuthenticated
    ]

    def post(self, request, deck_pk=None,tag_pk=None):
        deck = get_object_or_404(user_decks(request.user),pk=deck_pk)
        tag = get_object_or_404(accessible_tags(request.user),pk=tag_pk)
        if deck.tags.filter(pk=tag.pk).exists():
            return Response({"detail":"tag already added to the deck"},status=status.HTTP_400_BAD_REQUEST)
        deck.tags.add(tag)
        return Response({"detail":"tag added successfully"},status=status.HTTP_200_OK)

    def delete(self, request, deck_pk=None, tag_pk=None):
        deck = get_object_or_404(user_decks(request.user),pk=deck_pk)
        tag = get_object_or_404(accessible_tags(request.user),pk=tag_pk)
        if not deck.tags.filter(pk=tag.pk).exists():
            return Response({"detail":"tag does not belong to the deck"},status=status.HTTP_400_BAD_REQUEST)
        deck.tags.remove(tag)
        return Response({"detail":"tag removed successfully"},status=status.HTTP_200_OK)

class DeckTagGetAction(APIView):
    permission_classes=[
        IsAuthenticated
    ]
    def get(self, request, deck_pk=None):
        deck = get_object_or_404(accessible_decks(request.user),pk=deck_pk)
        serializer = TagReadSerializer(deck.tags.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
