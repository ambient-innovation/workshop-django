from rest_framework import serializers

from apps.cat.models import Cat, Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'id',
            'name',
        ]


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = [
            'id',
            'name',
            'colour',
        ]
