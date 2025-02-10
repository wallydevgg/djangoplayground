from django.db import models


class tblAcopiador(models.Model):
    intAcopiadorId = models.AutoField(primary_key=True)
    intRUC = models.IntegerField(max_length=8)
    strAcopiador = models.TextField(max_length=255)


class tblPlataforma(models.Model):
    intPlataformaId = models.AutoField(primary_key=True)
    strPlataforma = models.CharField(max_length=255)
    strRUC = models.CharField(max_length=20)
    strDireccion = models.CharField(max_length=255)
    intEstadoDefault = models.IntegerField()
    bitRegistroDefault = models.BooleanField()


class tblCertificado(models.Model):
    intCertificadoId = models.AutoField(primary_key=True)
    intPlataformaId = models.ForeignKey(tblPlataforma, on_delete=models.CASCADE)
    strCertificado = models.CharField(max_length=255)


class tblCliente(models.Model):
    intClienteId = models.AutoField(primary_key=True)
    strTipo = models.CharField(max_length=11)
    strSubTipo = models.CharField(max_length=11)
    intRUC = models.IntegerField(max_length=8)
    strRazon = models.CharField(max_length=11)
    strDireccion = models.CharField(max_length=50)
    intTelefono = models.IntegerField(max_length=12)
    fltFactorPeso = models.DecimalField(decimal_places=2, max_digits=5)
    intPesadorCreacionId = models.IntegerField(null=True)
    dtFechaCreacion = models.DateTimeField(auto_now_add=True)
    intPesadorModificacionId = models.IntegerField(null=True)
    dtFechaModificacion = models.DateTimeField(auto_now=True)

    # category=models.ForeignKey(
    #  Category,
    #  on_delete=models.CASCADE
    #  related_name='products'
    # )


#  class Meta:
#      db_table = "tblCliente"

#  def __str__(self):
#      return self.name


class tblEstado(models.Model):
    intEstadoId = models.AutoField(primary_key=True)
    strEstado = models.CharField(max_length=255)


class tblPesador(models.Model):
    intPesadorId = models.AutoField(primary_key=True)
    strNombres = models.CharField(max_length=255)
    strApellidos = models.CharField(max_length=255)
    strLogin = models.CharField(max_length=100)
    strPwd = models.CharField(max_length=100)


class tblProcedencia(models.Model):
    intProcedenciaId = models.AutoField(primary_key=True)
    strProcedencia = models.CharField(max_length=255)


class tblProducto(models.Model):
    intProductoId = models.AutoField(primary_key=True)
    strProducto = models.CharField(max_length=255)


class tblSerieDoc(models.Model):
    intSerieDocId = models.AutoField(primary_key=True)
    strSerieDoc = models.CharField(max_length=50)
    intCertificadoId = models.ForeignKey(tblCertificado, on_delete=models.CASCADE)


class tblTransportista(models.Model):
    intTransportistaId = models.AutoField(primary_key=True)
    strTransportista = models.CharField(max_length=255)


class tblEntrada(models.Model):
    intEntradaId = models.AutoField(primary_key=True)
    intCertificadoId = models.ForeignKey(tblCertificado, on_delete=models.CASCADE)
    strSerieDoc = models.ForeignKey(tblSerieDoc, on_delete=models.CASCADE)
    intProductoId = models.ForeignKey(tblProducto, on_delete=models.CASCADE)
    intClienteId = models.ForeignKey(tblCliente, on_delete=models.CASCADE)
    intTransportistaId = models.ForeignKey(tblTransportista, on_delete=models.CASCADE)
    strGuia = models.CharField(max_length=50)
    strPlaca = models.CharField(max_length=20)
    intEstadoId = models.ForeignKey(tblEstado, on_delete=models.CASCADE)
    dtFechaCreacion = models.DateTimeField(auto_now_add=True)
    dtFechaModificacion = models.DateTimeField(auto_now=True)


class tblSalida(models.Model):
    intSalidaId = models.AutoField(primary_key=True)
    intEntradaId = models.ForeignKey(tblEntrada, on_delete=models.CASCADE)
    intEstadoId = models.ForeignKey(tblEstado, on_delete=models.CASCADE)
    dtFechaCreacion = models.DateTimeField(auto_now_add=True)
    dtFechaModificacion = models.DateTimeField(auto_now=True)


class tblTarifa(models.Model):
    intTarifaId = models.AutoField(primary_key=True)
    strTarifa = models.CharField(max_length=255)
    strMoneda = models.CharField(max_length=10)
    intMonto = models.DecimalField(max_digits=10, decimal_places=2)


class tblZona(models.Model):
    intZonaId = models.AutoField(primary_key=True)
    strZona = models.CharField(max_length=255)
