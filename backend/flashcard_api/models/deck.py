from django.db import models 
from django.contrib.auth.models import User
from .tag import Tag

class Deck(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['is_public'])
        ]
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="decks")

    tags = models.ManyToManyField(Tag, related_name="decks", blank=True)
