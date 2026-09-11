from django.contrib import admin
from .models import Deck, Flashcard, Progress, Review
# Register your models here.
admin.site.register(Deck)
admin.site.register(Flashcard)
admin.site.register(Progress)
admin.site.register(Review)

#TO-DO: when creating a flashcard it should automatically get progress entry