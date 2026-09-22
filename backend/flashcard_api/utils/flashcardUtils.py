from ..models import Deck, Flashcard
from django.db.models import Q

def user_flashcards(user):
    if user.is_staff:
        return Flashcard.objects.all()

    return Flashcard.objects.filter(deck__owner=user)

def public_flashcards(user):
    if user.is_staff:
        return Flashcard.objects.all()
    return Flashcard.objects.filter(deck__is_public=True)

def accessible_flashcards(user):
    if user.is_staff:
        return Flashcard.objects.all()
    return Flashcard.objects.filter(Q(deck__is_public=True) | Q(deck__owner = user) )


def learning_flashcards(user):
    if user.is_staff:
        return Flashcard.objects.all()
    return Flashcard.objects.filter(Q(deck__owner=user) | Q(deck__bookmarks__user=user)).distinct()


