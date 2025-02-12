from django.db import models


class tblSupervCancha(models.Model):
    intSupervCanchaId = models.AutoField(primary_key=True)
    strNombreSuperV = models.CharField(max_length=150)
    strPlaca = models.CharField(max_length=25)
    fltPeso = models.DecimalField(decimal_places=2, max_digits=10)
    dtmFecha = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "tblSupervCancha"


class tblPersSeguridad(models.Model):
    intPersSeguridadId = models.AutoField(primary_key=True)
    strNombreSeguridad = models.CharField(max_length=150)
    strTipoMarca = models.CharField(max_length=50)
    strPlaca = models.CharField(max_length=25)
    strConductor = models.CharField(max_length=50)
    dtmFechaIngreso = models.DateField(auto_now=True)

    class Meta:
        db_table = "tblPersSeguridad"


class tblAtencionClte(models.Model):
    intAtencionClteId = models.AutoField(primary_key=True)
    strPlaca = models.CharField(max_length=25)
    fltPeso = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        db_table = "tblAtencionClte"


class tblPlataforma(models.Model):
    intPlataformaId = models.AutoField(primary_key=True)
    strPlataforma = models.CharField(max_length=255)
    intRUC = models.IntegerField(default=0)
    strDireccion = models.CharField(max_length=255)
    intSerieDocIdDefault = models.IntegerField(null=True)
    intTarifaIdDefault = models.IntegerField(null=True)
    blnRegistroDefault = models.BooleanField(default=False)

    class Meta:
        db_table = "tblPlataforma"

    def __str__(self):
        return self.strPlataforma


class tblCertificado(models.Model):
    intCertificadoId = models.AutoField(primary_key=True)
    fkPlataformald = models.ForeignKey(
        tblPlataforma, on_delete=models.CASCADE, null=True
    )
    dtFechaIni = models.DateTimeField(auto_now_add=True)
    dtFechaFin = models.DateField(auto_now=True)
    intCertEstado = models.IntegerField(null=True)

    class Meta:
        db_table = "tblCertificado"

    def __str__(self):
        return f"CertificadoId {self.intCertificadoId}"


class tblSerieDoc(models.Model):
    intSerieDocId = models.AutoField(primary_key=True)
    strSerieDocAbrev = models.CharField(max_length=25)
    strSerieDocDesc = models.CharField(max_length=50)
    intCorrelActual = models.IntegerField(null=True)

    class Meta:
        db_table = "tblSerieDoc"

    def __str__(self):
        return f"SerieDocId {self.intSerieDocId}"


class tblProcedencia(models.Model):
    intProcedenciaId = models.AutoField(primary_key=True)
    strProcedencia = models.CharField(max_length=255)

    class Meta:
        db_table = "tblProcedencia"

    def __str__(self):
        return f"Procedencia?: {self.intProcedenciaId} {self.strProcedencia}"


class tblTransportista(models.Model):
    intTransportistaId = models.AutoField(primary_key=True)
    intRUC = models.CharField(max_length=20, null=True)
    strTransportista = models.CharField(max_length=255)

    class Meta:
        db_table = "tblTransportista"

    def __str__(self):
        return f"Transportista {self.strTransportista}"


class tblProducto(models.Model):
    intProductoId = models.AutoField(primary_key=True)
    strProducto = models.CharField(max_length=255)

    class Meta:
        db_table = "tblProducto"

    def __str__(self):
        return f"Producto {self.strProducto}"


class tblAcopiador(models.Model):
    intAcopiadorId = models.AutoField(primary_key=True)
    strRUC = models.CharField(max_length=20, null=True)
    strAcopiador = models.CharField(max_length=255)

    class Meta:
        db_table = "tblAcopiador"

    def __str__(self):
        return f"Acopiador {self.strAcopiador}"


class tblPesador(models.Model):
    intPesadorId = models.AutoField(primary_key=True)
    strNombres = models.CharField(max_length=255)
    strApellidos = models.CharField(max_length=255)
    strLogin = models.CharField(max_length=100)
    strPwd = models.CharField(max_length=100)

    class Meta:
        db_table = "tblPesador"

    def __str__(self):
        return f"Pesador?: {self.strNombres} {self.strApellidos}"


class tblCliente(models.Model):
    intClienteId = models.AutoField(primary_key=True)
    strTipo = models.CharField(max_length=50)
    strSubTipo = models.CharField(max_length=50)
    intRUC = models.CharField(max_length=20, null=True)
    strRazon = models.CharField(max_length=255)
    strDireccion = models.CharField(max_length=255)
    strTelefono = models.CharField(max_length=25, default=0)
    fltFactorPeso = models.DecimalField(max_digits=2, decimal_places=1)
    intPesadorCreacionId = models.ForeignKey(
        tblPesador, on_delete=models.CASCADE, null=True
    )
    dtFechaCreacion = models.DateTimeField(auto_now_add=True)
    intPesadorModificacionId = models.IntegerField(null=True)
    dtFechaModificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tblCliente"

    def __str__(self):
        return self.strRazon


class tblZona(models.Model):
    intZonaId = models.AutoField(primary_key=True)
    intCodigo = models.IntegerField(null=True)
    strZona = models.CharField(max_length=255)

    class Meta:
        db_table = "tblZona"

    def __str__(self):
        return self.strZona


class tblTarifa(models.Model):
    intTarifaId = models.AutoField(primary_key=True)
    strTarifa = models.CharField(max_length=40)
    intNroEjes = models.IntegerField(null=True)
    strMoneda = models.CharField(max_length=10)
    intMonto = models.IntegerField(default=0)

    class Meta:
        db_table = "tblTarifa"

    def __str__(self):
        return self.strTarifa


class tblEstado(models.Model):
    intEstadoId = models.AutoField(primary_key=True)
    strEstado = models.CharField(max_length=255)

    class Meta:
        db_table = "tblEstado"

    def __str__(self):
        return self.strEstado


class tblRecurrente(models.Model):
    intRecurrenteId = models.ForeignKey(tblCliente, on_delete=models.CASCADE, null=True)
    strRecurrenciaEstado = models.CharField(max_length=25)

    class Meta:
        db_table = "tblRecurrente"

    def __str__(self):
        return f"Recurrente?: {self.strRecurrenciaEstado}"


class tblEntrada(models.Model):
    intEntradaId = models.AutoField(primary_key=True)
    intCertificadoId = models.ForeignKey(
        tblCertificado, on_delete=models.CASCADE
    )  # certificado
    intSerieDocId = models.ForeignKey(tblSerieDoc, on_delete=models.CASCADE)  # seriedoc
    intProcedenciaId = models.ForeignKey(
        tblProcedencia, on_delete=models.CASCADE
    )  # procedencia
    intClienteId = models.ForeignKey(tblCliente, on_delete=models.CASCADE)  # cliente

    # Vehiculo - espacios dejados en blanco porque son llenados en el software de balanza
    strTipoMarca = models.CharField(max_length=50)
    strPlaca1 = models.CharField(max_length=25)
    strPlaca2 = models.CharField(max_length=25)
    strConductor = models.CharField(max_length=50)

    intTransportistaId = models.ForeignKey(
        tblTransportista, on_delete=models.CASCADE
    )  # transportista

    strNroGuia = models.CharField(max_length=50)
    strNroGuiaT = models.CharField(max_length=50)
    strPlaca = models.CharField(max_length=20)

    intProductoId = models.ForeignKey(tblProducto, on_delete=models.CASCADE)  # Producto

    intNroSacos = models.IntegerField(default=0)

    intAcopiadorId = models.ForeignKey(
        tblAcopiador, on_delete=models.CASCADE
    )  # acopiador

    intZonaId = models.ForeignKey(tblZona, on_delete=models.CASCADE)  # Zona

    strObservacion = models.CharField(max_length=150)
    blnFlagRegulizar = models.BooleanField(default=False)
    intPesoInicial = models.IntegerField(default=0)

    # tarifa
    intTarifaId = models.ForeignKey(tblTarifa, on_delete=models.CASCADE)

    # estado
    intEstadoId = models.ForeignKey(tblEstado, on_delete=models.CASCADE)

    blEliminado = models.BooleanField(default=False)

    strEstacionPC = models.CharField(max_length=50)

    intPesadorCreacionId = models.ForeignKey(
        tblPesador, on_delete=models.CASCADE, related_name="entradasPesador_creadas"
    )
    dtFechaCreacion = models.DateTimeField(auto_now_add=True)

    intPesadorModificacionId = models.ForeignKey(
        tblPesador, on_delete=models.CASCADE, related_name="entradasPesador_modificadas"
    )
    dtFechaModificacion = models.DateTimeField(auto_now=True)

    intRecurrenteId = models.ForeignKey(tblRecurrente, on_delete=models.CASCADE)

    class Meta:
        db_table = "tblEntrada"

    def __str__(self):
        return self.intEntradaId


class tblSalida(models.Model):
    intEntrada = models.ForeignKey(tblEntrada, on_delete=models.CASCADE)
    intPesoFinal = models.IntegerField(default=0)

    intPesadorCreacionId = models.ForeignKey(
        tblPesador, on_delete=models.CASCADE, related_name="salidasPesador_creadas"
    )
    intPesadorModificacionId = models.ForeignKey(
        tblPesador, on_delete=models.CASCADE, related_name="salidasPesador_modificadas"
    )

    dtFechaModificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tblSalida"

    def __str__(self):
        return f"PesoFinal?: {self.intPesoFinal}"
