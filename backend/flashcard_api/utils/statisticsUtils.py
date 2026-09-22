from ..models import Flashcard, Progress, Review
from django.utils import timezone
from django.db.models import Avg, Max

def deck_user_statistics(deck,user):
    now = timezone.now()

    progresses = Progress.objects.filter(flashcard__deck=deck,user=user)
    reviews = Review.objects.filter(flashcard__deck=deck,user=user)
    total_flashcards= Flashcard.objects.filter(deck=deck).count()
    started_flashcards= progresses.count()
    due_flashcards= progresses.filter(due_at__lte=now).count()
    total_reviews = reviews.count()
    reviews_today = reviews.filter(reviewed_at__date = now.date()).count()
    cards_reviewed_today = reviews.filter( reviewed_at__date=now.date()).values("flashcard").distinct().count()
    avg_ease_factor = progresses.aggregate(average=Avg("ease_factor"))["average"]
    last_reviewed_at= reviews.aggregate(last_reviewed=Max("reviewed_at"))["last_reviewed"]
    return {
        "total_flashcards":total_flashcards,
        "started_flashcards":started_flashcards,
        "new_cards":(total_flashcards - started_flashcards),
        "due_flashcards":due_flashcards,
        "total_reviews":total_reviews,
        "cards_reviewed_today":cards_reviewed_today,
        "reviews_today":reviews_today,
        "avg_ease_factor":avg_ease_factor,
        "last_reviewed_at":last_reviewed_at,

    }