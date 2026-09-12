from django.db import models 

class Deck(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
