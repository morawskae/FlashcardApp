from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (DeckViewSet, FlashcardDetailedAPIView, 
                    FlashcardReviewAction, DeckProgressAction, FlashcardProgressAction)

router = DefaultRouter()
router.register(r'decks',DeckViewSet,basename='decks')
urlpatterns = [
    path('',include(router.urls)),
    path('flashcards/<int:pk>/',FlashcardDetailedAPIView.as_view(),name="flashcard-detail"),
    path('flashcards/<int:pk>/review/',FlashcardReviewAction.as_view(),name="flashcard-review"),
    path('decks/<int:pk>/flashcards/due',DeckProgressAction.as_view(),name="deck-progress"),
    path('flashcards/<int:pk>/progress/',FlashcardProgressAction.as_view(), name="flashcard-progress")
]