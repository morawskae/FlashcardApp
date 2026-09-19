from django.db import models 
from django.contrib.auth.models import User
class Deck(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True,default='')
    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="decks")
