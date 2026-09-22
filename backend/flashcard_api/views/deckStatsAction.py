from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from ..utils import learning_decks, deck_user_statistics
from rest_framework.response import Response
from rest_framework import status

class DeckStatsAction(APIView):
    permission_classes=[
        IsAuthenticated
    ]

    def get(self,request, pk=None):
        deck = get_object_or_404(learning_decks(request.user),pk=pk)
        statistics = deck_user_statistics(deck,request.user)
        return Response(statistics, status=status.HTTP_200_OK)