from rest_framework.views import APIView
from ..models import Progress
from django.shortcuts import get_object_or_404
from ..serializers import ProgressReadSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..utils import accessible_flashcards

class FlashcardProgressAction(APIView):
        
    permission_classes = [
        IsAuthenticated,
    ]
        
    def get(self, request, pk=None):
        flashcard = get_object_or_404(accessible_flashcards(request.user), pk=pk)
        progress = get_object_or_404(Progress,flashcard=flashcard)
        serializer = ProgressReadSerializer(progress)
        return Response(serializer.data, status=status.HTTP_200_OK)