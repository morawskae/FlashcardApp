from .sm2 import sm2_algorithm
from flashcard_api.models import Progress, Rating, Review
from django.db import transaction

def sm2_scheduler(progress:Progress, rating:Rating)-> Progress:
    with transaction.atomic():
        sm2_algorithm(progress=progress, rating=rating)
        progress.save()
        Review.objects.create_review(progress.flashcard, rating)
    return progress