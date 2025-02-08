from django.db import models


class Acopiador(models.Model):
    intAcopiadorId = models.AutoField(primary_key=True)
    intRUC= models.IntegerField(max_length=8)
    strAcopiador = models.TextField(max_length=255)

class Certificado(models.Model):
    intCertificadoId = models.AutoField(primary_key=True)
    intPlataformaId = models.IntegerField()

class Cliente(models.Model):
    intClienteId = models.AutoField(primary_key=True)
    strTipo= models.CharField(max_length=11)
    strSubTipo= models.CharField(max_length=11)
    intRUC= models.IntegerField(max_length=8)
    strRazon= models.CharField(max_length=11)
    strDireccion= models.CharField(max_length=50)
    intTelefono= models.IntegerField(max_length=12)
    fltFactorPeso=models.DecimalField(decimal_places=2, max_digits=12)
    intPesadorCreacionId= models.AutoField(primary_key=True)
    dtFechaCreacion= models.DateTimeField(auto_now_add=True)
    intPesadorModificacionId=models.IntegerField(null=True)
    dtFechaModificacion= models.DateTimeField(auto_now=True)

