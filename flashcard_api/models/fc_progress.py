from django.db import models 
from .flashcard import Flashcard

class FcProgress(models.Model):
    due_at = models.DateField()
    last_reviewed_at = models.DateTimeField()

    successful_repetitions = models.PositiveIntegerField(default=0)
    ease_factor = models.FloatField(default=2.5)
    interval = models.PositiveIntegerField(default=0)

    flashcard = models.OneToOneField(Flashcard, on_delete=models.CASCADE, related_name="progress")