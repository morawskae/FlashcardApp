from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (DeckViewSet, FlashcardDetailedAPIView, 
                    FlashcardReviewAction, DeckProgressAction, FlashcardProgressAction,
                    DeckPublicAction, DeckBookmarkedAction)
from .views.auth import (RegisterApiView, LoginApiView, LogoutApiView )
router = DefaultRouter()
router.register(r'decks',DeckViewSet,basename='decks')
urlpatterns = [
    path('decks/public/',DeckPublicAction.as_view(),name="decks-public"),
    path('decks/bookmarked/',DeckBookmarkedAction.as_view(),name="decks-bookmarked"),
    path('',include(router.urls)),
    path('flashcards/<int:pk>/',FlashcardDetailedAPIView.as_view(),name="flashcard-detail"),
    path('flashcards/<int:pk>/review/',FlashcardReviewAction.as_view(),name="flashcard-review"),
    path('decks/<int:pk>/flashcards/due/',DeckProgressAction.as_view(),name="deck-progress"),
    path('flashcards/<int:pk>/progress/',FlashcardProgressAction.as_view(), name="flashcard-progress"),
    path('auth/register/', RegisterApiView.as_view(), name="register"),
    path('auth/login/',LoginApiView.as_view(), name="login"),
    path('auth/logout/',LogoutApiView.as_view(), name="logout") 
]