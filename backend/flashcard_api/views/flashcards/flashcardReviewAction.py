from ...models import Rating, Progress, Review
from rest_framework.response import Response
from rest_framework import status
from ...services import sm2_scheduler
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from ...serializers import ReviewReadSerializer
from rest_framework.permissions import IsAuthenticated
from ...utils import learning_flashcards 

class FlashcardReviewAction(APIView):

    permission_classes = [
        IsAuthenticated]

    def post(self, request,pk=None):
        flashcard = get_object_or_404(learning_flashcards(request.user), pk=pk)
        rating = request.data.get("rating")
        if(rating is None):
            return Response({"detail":"Rating is required"},status=status.HTTP_400_BAD_REQUEST)
        try:
            rating = Rating(int(rating))
        except(ValueError, TypeError):
            return Response({"detail":"Invalid Rating"},status=status.HTTP_400_BAD_REQUEST)
        progress, _ = Progress.objects.get_or_create(
        flashcard=flashcard,
        user=request.user)
        sm2_scheduler(progress, rating, request.user)
        return Response({"detail":"Flashcard reviewed successfully"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        flashcard = get_object_or_404(learning_flashcards(request.user), pk=pk)
        reviews = Review.objects.filter(flashcard=flashcard, user=request.user)
        serializer = ReviewReadSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

