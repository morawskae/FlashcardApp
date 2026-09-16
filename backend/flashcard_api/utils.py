from .models import Deck, Flashcard


def accessible_decks(user):
    if user.is_staff:
        return Deck.objects.all()

    return Deck.objects.filter(owner=user)


def accessible_flashcards(user):
    if user.is_staff:
        return Flashcard.objects.all()

    return Flashcard.objects.filter(
        deck__owner=user
    )