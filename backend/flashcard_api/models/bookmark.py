from django.db import models
from django.contrib.auth.models import User
from ..models import Deck

class BookmarkManager(models.Manager):
    def create_bookmark(self,deck:Deck, user:User):
        bookmark = self.create(deck=deck,user=user)
        return bookmark

class Bookmark(models.Model):
    class Meta:
        constraints =[
            models.UniqueConstraint(
                fields=["user","deck"],
                name="unique_user_deck_bookmark"
            )
        ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmarks")
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="bookmarks")

    objects = BookmarkManager()