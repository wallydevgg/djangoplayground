from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=160)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "categories"

        def __str__(self):
            return self.name
