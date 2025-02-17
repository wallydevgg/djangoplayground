from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # overwritenn created fields
    email = models.EmailField(unique=True)
    avatar = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

    REQUIRED_FIELDS = ["email", "password"]

    # metodos de instancia
    def create_user(self, **kwargs):
        record = self.model(**kwargs)
        record.set_password(kwargs["password"])
        record.save()
        return record
