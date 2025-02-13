from django.db import models

# Create your models here.
class tblIngresoVehiculo(models.Model):
    intIngresoVeId=models.AutoField(primary_key=True)
    strPlacaVehiculo=models.CharField(max_length=100)
    strNombreConductor=models.CharField(max_length=150)

    class Meta:
        db_table='tblIngresoVehiculo'