# restaurant/views.py
from rest_framework import generics
from .models import Restaurant, Menu, MenuItem, Order
from .serializers import RestaurantSerializer, MenuSerializer, MenuItemSerializer, OrderSerializer, OrderCreateSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuList(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetail(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemList(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemDetail(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateByUser(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        customer = self.kwargs['user_id']
        user = User.objects.filter(pk=customer)[0]
        serializer.save(customer=user)


class OrderListByUser(generics.ListAPIView):

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = User.objects.filter(pk=user_id)[0]
        return Order.objects.filter(customer=user)


class DishesByMenu(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        menuId = self.kwargs['pk']
        menu = Menu.objects.filter(pk=menuId)[0]
        dishes = MenuItem.objects.filter(menu=menu)
        return dishes
