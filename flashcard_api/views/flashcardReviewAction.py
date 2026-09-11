from ..models import Flashcard,Rating, Progress
from ..serializers import ( FlashcardWriteSerializer, FlashcardReadSerializer)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from ..services import schleduler

class FlashcardReviewAction():
    @action(detail=True, methods=["post"],url_path="review")
    def review(self, request,pk=None):
        flashcard = self.get_object()
        rating = request.data.get("rating")
        if(rating is None):
            return Response({"detail":"Rating is required"},status=status.HTTP_400_BAD_REQUEST)
        try:
            rating = Rating(int(rating))
        except(ValueError, TypeError):
            Response({"detail":"Invalid Rating"},status=status.HTTP_400_BAD_REQUEST)
        progress = Progress.objects.get(flashcard=flashcard)
        schleduler(progress, rating)
        return Response({"detail":"Flashcard reviewed successfully"}, status=status.HTTP_200_OK)