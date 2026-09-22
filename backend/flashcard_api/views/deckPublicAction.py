from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..utils import public_decks
from ..serializers import DeckListSerializer

class DeckPublicAction(APIView):
    permission_classes=[
        IsAuthenticated
    ]

    def get(self, request):
        decks = public_decks(request.user)
        serializer = DeckListSerializer(decks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)