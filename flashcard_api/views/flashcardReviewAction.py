from ..models import Rating, Progress, Flashcard, Review
from rest_framework.response import Response
from rest_framework import status
from ..services import sm2_scheduler
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from ..serializers import ReviewReadSerializer
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

    def get(self, request, pk=None):
        print("DEBUG XD")
        flashcard = get_object_or_404(Flashcard, pk=pk)
        reviews = Review.objects.filter(flashcard=flashcard)
        serializer = ReviewReadSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

