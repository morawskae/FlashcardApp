from django.db import models 
from .flashcard import Flashcard

class ProgressManager(models.Manager):
    def create_progress(self, flashcard):
        progress = self.create(flashcard=flashcard)
        return progress 
    
class Progress(models.Model):
    due_at = models.DateTimeField(auto_now_add=True)
    last_reviewed_at = models.DateTimeField(null=True)

    successful_repetitions = models.PositiveIntegerField(default=0)
    ease_factor = models.FloatField(default=2.5)
    interval = models.PositiveIntegerField(default=0)

    flashcard = models.OneToOneField(Flashcard, on_delete=models.CASCADE, related_name="progress")

    objects = ProgressManager()