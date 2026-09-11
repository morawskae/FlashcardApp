from django.db import models
from .flashcard import Flashcard
from django.utils import timezone

class Rating(models.IntegerChoices):
    AGAIN = 2, "Again"
    HARD = 3, "Hard"
    GOOD = 4, "Good"
    EASY= 5, "Easy"

class ReviewManager(models.Manager):
    def create_review(self, flashcard, rating:Rating):
        review = self.create(rating = rating, flashcard = flashcard)
        return review

class Review(models.Model):
    reviewed_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=Rating.choices)
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE,related_name="reviews")

    objects = ReviewManager()

