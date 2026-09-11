from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeckViewSet, FlashcardDetailedAPIView

router = DefaultRouter()
router.register(r'decks',DeckViewSet,basename='decks')
router.register(r'flashcards',FlashcardDetailedAPIView,basename='flashcards')

urlpatterns = [
    path('',include(router.urls))
]