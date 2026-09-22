from rest_framework.views import APIView
from ..models import Progress
from django.shortcuts import get_object_or_404
from ..serializers import ProgressReadSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..utils import user_flashcards

class FlashcardProgressAction(APIView):
        
    permission_classes = [
        IsAuthenticated,
    ]
        
    def get(self, request, pk=None):
        flashcard = get_object_or_404(user_flashcards(request.user), pk=pk) #in the future include bookmarked
        progress, _ = Progress.objects.get_or_create(
        flashcard=flashcard,
        user=request.user)
        serializer = ProgressReadSerializer(progress)
        return Response(serializer.data, status=status.HTTP_200_OK)