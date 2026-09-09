from django.db import models 
from .flashcard import Flashcard
class FcProgress(models.Model):
    due_at = models.DateField()
    last_reviewed_ar = models.DateTimeField()
    repetitions = models.IntegerField()
    ease_factor = models.FloatField()
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)