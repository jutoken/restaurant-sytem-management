# restaurant/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    website = models.URLField()

    def __str__(self) -> str:
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [("pending","pending"),("done","done")]
    customer = models.ForeignKey(User, on_delete=models.Case)
    items = models.ManyToManyField(MenuItem)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default="pending")

    def __str__(self) -> str:
        return self.status

    def calculate_total_cost(self):
        total = 0
        for item in self.items.all():
            total += item.price

        return total


@receiver(m2m_changed, sender=Order.items.through)
def calculate_total_cost_m2m_changed_receiver(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove"]:
        instance.total_cost = instance.calculate_total_cost()
        instance.save()
