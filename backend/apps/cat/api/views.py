from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.cat.api import serializers
from apps.cat.models import Cat, Food


class CatViewSet(mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CatSerializer

    def get_queryset(self):
        return Cat.objects.visible_for(self.request.user)


class FoodViewSet(mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.FoodSerializer
    queryset = Food.objects.all()
