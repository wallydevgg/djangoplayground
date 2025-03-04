from django.db import models


# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "coupons"

    def __str__(self):
        return self.code
