from django.db import models

class FcReview(models.Model):
    rating = {
        0:"AGAIN",
        1:"HARD",
        2:"GOOD",
        3:"EASY"
        }
    reviewed_at = models.DateTimeField()