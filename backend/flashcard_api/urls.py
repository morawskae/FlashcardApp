from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (DeckViewSet, FlashcardDetailedAPIView, 
                    FlashcardReviewAction, DeckProgressAction, FlashcardProgressAction,
                    DeckPublicAction, BookmarkPostDelAction, BookmarkedDecksGetAction,
                    DeckStatsAction, TagViewSet,
                    DeckTagGetAction, DeckTagPostDelAction)
from .views.auth import (RegisterApiView, LoginApiView, LogoutApiView )
router = DefaultRouter()
router.register(r'decks',DeckViewSet,basename='decks')
router.register(r'tags',TagViewSet,basename='tags')
urlpatterns = [
    path('decks/public/',DeckPublicAction.as_view(),name="decks-public"),
    path('decks/bookmarked/',BookmarkedDecksGetAction.as_view(),name="decks-bookmarked"),
    path('decks/<int:pk>/stats/',DeckStatsAction.as_view(),name="decks-stats"),
    path('decks/<int:pk>/bookmarked/',BookmarkPostDelAction.as_view(),name="deck-bookmarked"),
    path('',include(router.urls)),
    path('flashcards/<int:pk>/',FlashcardDetailedAPIView.as_view(),name="flashcard-detail"),
    path('flashcards/<int:pk>/review/',FlashcardReviewAction.as_view(),name="flashcard-review"),
    path('decks/<int:pk>/flashcards/due/',DeckProgressAction.as_view(),name="decks-progress"),
    path('flashcards/<int:pk>/progress/',FlashcardProgressAction.as_view(), name="flashcard-progress"),
    path('auth/register/', RegisterApiView.as_view(), name="register"),
    path('auth/login/',LoginApiView.as_view(), name="login"),
    path('auth/logout/',LogoutApiView.as_view(), name="logout"),
    path('decks/<int:deck_pk>/tags/<int:tag_pk>/', DeckTagPostDelAction.as_view(),name="deck-tag"),
    path('decks/<int:deck_pk>/tags/', DeckTagGetAction.as_view(),name="deck-tags")
]