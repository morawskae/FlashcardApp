from django.db import models
from .flashcard import Flashcard
from django.contrib.auth.models import User

class Rating(models.IntegerChoices):
    AGAIN = 2, "Again"
    HARD = 3, "Hard"
    GOOD = 4, "Good"
    EASY= 5, "Easy"

class ReviewManager(models.Manager):
    def create_review(self, flashcard, rating:Rating, user:User):
        review = self.create(rating = rating, flashcard = flashcard,user=user)
        return review

class Review(models.Model):
    reviewed_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=Rating.choices)
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE,related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")

    objects = ReviewManager()

