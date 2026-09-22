from .models import Deck, Flashcard
from django.db.models import Q

def user_decks(user):
    if user.is_staff:
        return Deck.objects.all()

    return Deck.objects.filter(owner=user)

def public_decks(user):
    if user.is_staff:
        return Deck.objects.all()
    return Deck.objects.filter(is_public = True)

def accessible_decks(user):
    if user.is_staff:
        return Deck.objects.all()
    return Deck.objects.filter(Q(is_public = True) | Q(owner=user))

def user_flashcards(user):
    if user.is_staff:
        return Flashcard.objects.all()

    return Flashcard.objects.filter(
        deck__owner=user
    )

def public_flashcards(user):
    if user.is_staff:
        return Flashcard.objects.all()
    return Flashcard.objects.filter(deck__is_public=True)

def accessible_flashcards(user):
    if user.is_staff:
        return Flashcard.objects.all()
    return Flashcard.objects.filter(Q(deck__is_public=True) | Q(deck__owner = user) )