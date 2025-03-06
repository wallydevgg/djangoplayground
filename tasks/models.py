from django.db import models


class Exchange(models.Model):
    buy_price = models.DecimalField(max_digits=5, decimal_places=2)
    sell_price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "exchanges"

    def __str__(self):
        return f"{self.buy_price} - {self.sell_price}"
