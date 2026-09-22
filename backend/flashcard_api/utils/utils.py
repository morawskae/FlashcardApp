from ..models import Deck, Flashcard
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

def bookmarked_decks(user):
    if user.is_staff:
        return Deck.objects.all()
    return Deck.objects.filter(bookmarks__user=user)

def learning_decks(user):
    if user.is_staff:
        return Deck.objects.all()

    return Deck.objects.filter(Q(owner=user) | Q(bookmarks__user=user)).distinct()


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

def has_bookmarks(deck):
    return deck.bookmarks.count()>0

