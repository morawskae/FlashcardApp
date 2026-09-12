from rest_framework.views import APIView
from ..models import Flashcard, Progress
from django.shortcuts import get_object_or_404
from ..serializers import ProgressReadSerializer
from rest_framework.response import Response
from rest_framework import status

class FlashcardProgressAction(APIView):
    def get(self, request, pk=None):
        flashcard = get_object_or_404(Flashcard, pk=pk)
        progress = Progress.objects.get(flashcard=flashcard)
        serializer = ProgressReadSerializer(progress)
        return Response(serializer.data, status=status.HTTP_200_OK)