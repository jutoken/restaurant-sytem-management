# restaurant/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('restaurants/', RestaurantList.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view(),
         name='restaurant-detail'),
    path('menus/', MenuList.as_view(), name='menu-list'),
    path('menus/<int:pk>/', MenuDetail.as_view(), name='menu-detail'),
    path('menus/<int:pk>/meals/', DishesByMenu.as_view(), name='meals-by-menu'),
    path('meals/', MenuItemList.as_view(), name='meals-list'),
    path('meals/<int:pk>/', MenuItemDetail.as_view(), name='meals-detail'),
    path('users/<int:user_id>/orders/add/',
         OrderCreateByUser.as_view(), name='create-order'),
    path('users/<int:user_id>/orders/',
         OrderListByUser.as_view(), name='list-order'),
]
