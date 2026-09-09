from django.db import models
from .flashcard import Flashcard

class FcReview(models.Model):

    class Rating(models.IntegerChoices):
        AGAIN = 0, "Again"
        HARD = 1, "Hard"
        GOOD = 2, "Good"
        EASY= 3, "Easy"

    reviewed_at = models.DateTimeField()
    rating = models.CharField(choices=Rating.choices)

    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE,related_name="reviews")