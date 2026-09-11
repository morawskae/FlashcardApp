from ..models import Rating, Progress, Flashcard
from rest_framework.response import Response
from rest_framework import status
from ..services import sm2_scheduler
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
class FlashcardReviewAction(APIView):

    def post(self, request,pk=None):
        flashcard = get_object_or_404(Flashcard, pk=pk)
        rating = request.data.get("rating")
        if(rating is None):
            return Response({"detail":"Rating is required"},status=status.HTTP_400_BAD_REQUEST)
        try:
            rating = Rating(int(rating))
        except(ValueError, TypeError):
            return Response({"detail":"Invalid Rating"},status=status.HTTP_400_BAD_REQUEST)
        progress = Progress.objects.get(flashcard=flashcard)
        sm2_scheduler(progress, rating)
        return Response({"detail":"Flashcard reviewed successfully"}, status=status.HTTP_200_OK)