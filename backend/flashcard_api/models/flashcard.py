from django.db import models
from .deck import Deck 

class Flashcard(models.Model):
    front_side = models.CharField(max_length=150)
    back_side = models.CharField(max_length=150)

    deck = models.ForeignKey(Deck, on_delete= models.CASCADE, related_name="flashcards")