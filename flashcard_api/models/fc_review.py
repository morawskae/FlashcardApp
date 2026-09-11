from django.db import models
from .flashcard import Flashcard

class Rating(models.IntegerChoices):
    AGAIN = 2, "Again"
    HARD = 3, "Hard"
    GOOD = 4, "Good"
    EASY= 5, "Easy"

class FcReview(models.Model):
    reviewed_at = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=Rating.choices)
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE,related_name="reviews")