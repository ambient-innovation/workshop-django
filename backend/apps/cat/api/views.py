from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.cat.api import serializers
from apps.cat.models import Cat, Food


class CatViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CatSerializer

    def get_queryset(self):
        return Cat.objects.all()

    @action(detail=True, methods=('get',))
    def change_food_for_colour_and_move_cats(self, request, *args, **kwargs):
        """
        1) All tabby cats now like tuna.
        2) All cats eating too much creme age faster.
        """
        cat_list = Cat.objects.filter(owner=request.user)

        for cat in cat_list:
            if cat.colour == Cat.ColourChoices.TABBY:
                cat.favourite_foods.add(Food.objects.get(name='Thunfisch'))

        for cat in cat_list:
            if Food.objects.get(name='Sahne') in cat.favourite_foods.all():
                cat.age = cat.age + 1
                cat.save()

        return Response({}, status=status.HTTP_200_OK)


class FoodViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.FoodSerializer
    queryset = Food.objects.all()
