from django.db import models 
from .flashcard import Flashcard
from django.contrib.auth.models import User

class ProgressManager(models.Manager):
    def create_progress(self, flashcard, user:User):
        progress = self.create(flashcard=flashcard,user=user)
        return progress 
    
class Progress(models.Model):
    class Meta:
        constraints =[
            models.UniqueConstraint(
                fields=["user","flashcard"],
                name="unique_user_flashcard_progress"
            )
        ]
    due_at = models.DateTimeField(auto_now_add=True)
    last_reviewed_at = models.DateTimeField(null=True)

    successful_repetitions = models.PositiveIntegerField(default=0)
    ease_factor = models.FloatField(default=2.5)
    interval = models.PositiveIntegerField(default=0)

    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE, related_name="progress")
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="progress")

    objects = ProgressManager()