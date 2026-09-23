from ..models import Deck
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

def has_bookmarks(deck):
    return deck.bookmarks.count()>0

def filter_decks(decks, search=None, tags=None):
    if search:
        decks = decks.filter(title__icontains=search)
    if tags:
        for tag in tags:
            decks = decks.filter(tags__id=tag)
    return decks.distinct()
