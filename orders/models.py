from django.db import models
from users.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    subtotal_price = models.DecimalField(max_digits=9, decimal_places=2)
    igv_price = models.DecimalField(max_digits=9, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    shipping_date = models.DateTimeField()
    status = models.CharField(max_length=30, default="Pendiente")

    class Meta:
        db_table = "orders"

    def __str__(self):
        return f"{self.user} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()

    class Meta:
        db_table = "order_items"

    def __str__(self):
        return f"{self.order} - {self.product} - {self.quantity}"
