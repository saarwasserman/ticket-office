
from rest_framework import serializers

from .models import Basket, BasketLine


class BasketLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketLine
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    basket_lines = BasketLineSerializer(many=True, read_only=True)

    class Meta:
        model = Basket
        fields = ['id', 'user', 'basket_lines']
