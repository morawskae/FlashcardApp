from rest_framework import viewsets
from ..serializers import TagReadSerializer, TagWriteSerializer
from rest_framework.permissions import IsAuthenticated
from ..utils import user_tags, accessible_tags

class TagViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.action in ["retrieve","list"]:
            return accessible_tags(self.request.user)
        return user_tags(self.request.user)

    permission_classes=[
        IsAuthenticated
    ]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_serializer_class(self):
        if self.action in ["retrieve","list"]:
            return TagReadSerializer
        return TagWriteSerializer