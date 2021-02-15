from .models import Basket, BasketLine, Event
from .serializers import BasketSerializer, BasketLineSerializer
from ..ordering.serializers import OrderSerializer
from ticket_office.ordering.models import Order, OrderLine
from ..common import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_framework import generics

from rest_framework.decorators import api_view


class BasketDetail(generics.RetrieveUpdateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class BasketLineList(generics.ListCreateAPIView):
    queryset = BasketLine.objects.all()
    serializer_class = BasketLineSerializer


class BasketLineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BasketLine.objects.all()
    serializer_class = BasketLineSerializer


@api_view(['POST'])  # baskets/<basket_id>/checkout/
def checkout(request, basket_id):

    basket_id = request.user.basket.id
    basket = Basket.objects.get(id=basket_id)

    order = Order.objects.create(
        user=request.user,
        order_total=0
    )
    total_price = 0
    for basket_line in BasketLine.objects.filter(basket=basket):
        order_line = OrderLine(
            ticket_amount=basket_line.ticket_amount,
            event=basket_line.event,
            order=order
        )
        total_price += order_line.ticket_amount * order_line.event.price
        order_line.save()

    order.order_total = total_price
    order.save()

    return Response(OrderSerializer(order).data)


@api_view(['POST'])  # baskets/<basket_id>/clear/
def clear(request, basket_id):
    basket_id = request.user.basket.id
    basket = Basket.objects.get(id=basket_id)

    BasketLine.objects.filter(basket=basket).delete()

    return Response(BasketSerializer(basket).data)
