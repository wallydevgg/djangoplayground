from django.db import models
from balanza.models import tblRecurrente


class tblMaestro(models.Model):
    intMaestroId = models.AutoField(primary_key=True)
    strNombre = models.CharField(max_length=50)
    strDescripcion = models.CharField(max_length=100)
    fltValor = models.DecimalField(decimal_places=16, max_digits=15)
    strUsuarioCreador = models.CharField(max_length=20)
    strUsuarioModificador = models.CharField(max_length=20)
    dtFechaCreacion = models.DateTimeField(auto_now_add=True)
    dtFechaModificacion = models.DateTimeField(auto_now=True)
    strEstado = models.CharField(max_length=10)

    class Meta:
        db_table = "tblMaestro"
        verbose_name = 'Maestro'
        verbose_name_plural = 'Maestros'

    def __str__(self):
        return f"Maestro?: {self.intMaestroId} {self.strDescripcion} {self.fltValor}"


class Proveedor(models.Model):
    TIPO_PROVEEDOR_CHOICES = [
        ('PN', 'Persona Natural'),
        ('PJ', 'Persona Juridica'),
    ]

    TIPO_DOC_CHOICES = [
        ('DNI', 'Documento Nacional de Identidad'),
        ('RUC', 'Registro Único de Contribuyentes'),
    ]

    ESTADO_CIVIL_CHOICES = [
        ('Soltero', 'Soltero'),
        ('Casado', 'Casado'),
        ('Divorciado', 'Divorciado'),
        ('Viudo', 'Viudo'),
    ]

    intIdProveedor = models.AutoField(primary_key=True)
    strTipoProveedor = models.CharField(max_length=40, choices=TIPO_PROVEEDOR_CHOICES, null=True)
    strTipoDoc = models.CharField(max_length=20, choices=TIPO_DOC_CHOICES, null=True)
    strRucDni = models.CharField(max_length=30, null=True)
    strRazonSocial = models.CharField(max_length=300, null=True)
    strNacionalidad = models.CharField(max_length=50, null=True)
    fltTonMensuales = models.DecimalField(null=True)
    blnCalculoEspecial = models.BooleanField(default=False)
    strDireccion = models.CharField(max_length=500, null=True)
    strFirmaPath = models.CharField(max_length=200, null=True)
    strOcupacion = models.CharField(max_length=100, default='')
    strTelefono = models.CharField(max_length=14, default='')
    strCorreo = models.CharField(max_length=200, default='')
    strPropositoRelacion = models.CharField(max_length=200, default='')
    strNroPartidaSUNARP = models.CharField(max_length=50, default='')
    strEstadoCivil = models.CharField(max_length=30, choices=ESTADO_CIVIL_CHOICES, default='')
    strNombreConyugue = models.CharField(max_length=200, default='')
    blnEsPEP = models.BooleanField(default=False)
    strCargoPEP = models.CharField(max_length=100, default='')
    strNombreOrganismoPEP = models.CharField(max_length=100, default='')
    strNombrePariente2doPEP = models.CharField(max_length=200, default='')
    blnEstadoBlackList = models.BooleanField(default=False)
    strUsuarioCreador = models.CharField(max_length=35,
                                         null=True)  # estos usuario se hara FK de la tabla de usuarios con roles de admin/superuser
    dtFechaCreacion = models.DateTimeField(auto_now_add=True)
    strUsuarioModifcador = models.CharField(max_length=35,
                                            null=True)  # estos usuario se hara FK de la tabla de usuarios con roles de admin/superuser
    dtmFechaModif = models.DateTimeField(auto_now=True)
    chrEstado = models.CharField(max_length=1, null=True)
    strFechaInicioActividades = models.DateField(null=True, blank=True)
    strResidencia = models.CharField(max_length=100, null=True)
    strFileProveedor = models.URLField(null=True)  # documentacion de proveedor - bucket
    strRecurrente = models.ForeignKey(tblRecurrente, null=True, on_delete=models.CASCADE, related_name='ProvRecurrente')

    class Meta:
        db_table = 'tblProveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.strRazonSocial


class tblDeuda(models.Model):
    NOMBRE_EMPRESA = [
        ('LJM', 'La Joya Mining'),
        ('LJC', 'La Joya Commercial'),
    ],
    TIPO_DEUDA = [
        ('DEUDA', 'DEUDA'),
        ('CASTIGO', 'CASTIGO'),
        ('RECONOCIMIENTO', 'RECONOCIMIENTO'),
    ],
    ESTADO_DEUDA = [
        ('PENDIENTE', 'PENDIENTE'),
        ('CANCELADO', 'CANCELADO'),
    ],
    TIPO_CONDICION = [
        ('COMERCIAL', 'COMERCIAL'),
        ('CONTABLE', 'CONTABLE'),
        ('LEGAL', 'LEGAL'),

    ],

    intIdDeuda = models.AutoField(primary_key=True)
    intIdProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    strEmpresa = models.CharField(max_length=50, choices=NOMBRE_EMPRESA, default='')
    strTipo = models.CharField(max_length=30, choices=TIPO_DEUDA, default='')
    strEstadoDeuda = models.CharField(max_length=30, choices=ESTADO_DEUDA, default='')
    fltDeuda = models.DecimalField(decimal_places=2, max_digits=15)
    fltDeudaSoles = models.DecimalField(decimal_places=2, max_digits=15)
    strCondicion = models.CharField(max_length=10, choices=TIPO_CONDICION, default='')
    strComentarios = models.CharField(max_length=1000, choices=TIPO_CONDICION, default='')
    strZona = models.CharField(max_length=50, null=True)
    dtFechaDeuda = models.DateTimeField(auto_now_add=True)
    dtFechaAmortizacion = models.DateTimeField(auto_now=True)
    strUsuarioCreador = models.CharField(max_length=35, null=True)
    dtmFechaCreacion = models.DateTimeField(auto_now_add=True)
    strUsuarioModificador = models.CharField(max_length=35, null=True)
    dtmFechaModificacion = models.DateTimeField(auto_now=True)
    strEstado = models.CharField(max_length=1, null=True)

    class Meta:
        db_table = 'tblDeuda'
        verbose_name = 'Deuda'
        verbose_name_plural = 'Deudas'

    def __str__(self):
        return f"Deuda?: {self.intIdDeuda} {self.intIdProveedor} {self.fltDeuda}"


class tblParametrosComProv(models.Model):
    intIdParamComProv = models.AutoField(primary_key=True)
    intIdProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    strProveedor = models.CharField(max_length=300, null=True)
    fltRecComMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltMargenMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltMaquilaMin = models.DecimalField(decimal_places=2, max_digits=15)
    fltMaquilaMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltConsumoMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltGastAdmMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltGastLabMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltPorcHumedMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltPesoMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltRecAgMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltLeyAgMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltLeyAgComMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltMargenAgMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltRecAgComMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltRecIntMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltMaquilaIntMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltConsumoIntMax = models.DecimalField(decimal_places=2, max_digits=15)
    fltTmsLiqMax = models.DecimalField(decimal_places=2, max_digits=15)
    strUsuarioCrea = models.DecimalField(decimal_places=2, max_digits=15)
    dtmFechaCrea = models.DateTimeField(auto_now_add=True)
    strUsuarioModif = models.CharField(max_length=35, null=True)
    dtmFechaModif = models.DateTimeField(auto_now=True)
    strEstado = models.CharField(max_length=1, null=True)

    class Meta:
        db_table = 'tblParametrosComProv'
        verbose_name = 'ParametrosComProv'
        verbose_name_plural = 'ParametrosComProv'

    def __str__(self):
        return self.intIdProveedor


class tblROpBlackList(models.Model):
    intIdBlackList = models.AutoField(primary_key=True)
    intIdProveedor = models.AutoField(primary_key=True)
    strDescripcion = models.CharField(max_length=200, null=True)
    blnEstadoAprobacion = models.BooleanField(default=False)
    blnAprobacion1 = models.BooleanField(default=False)
    blnAprobacion2 = models.BooleanField(default=False)
    dtmFechaAprobacion1 = models.DateTimeField(auto_now_add=True)
    dtmFechaAprobacion2 = models.DateTimeField(auto_now=True)
    strUsuarioAprobo1 = models.CharField(max_length=35, null=True)
    strUsuarioAprobo2 = models.CharField(max_length=35, null=True)
    strUsuarioCrea = models.CharField(max_length=35, null=True)
    dtmFechaCrea = models.DateTimeField(auto_now_add=True)
    strUsuarioModif = models.CharField(max_length=35, null=True)
    dtmFechaModif = models.DateTimeField(auto_now=True)
    strEstado = models.CharField(max_length=1, null=True)

    class Meta:
        db_table = 'tblROpBlackList'
        verbose_name = 'ROpBlackList'
        verbose_name_plural = 'ROpBlackList'

    def __str__(self):
        return self.intIdProveedor


class tblROpCuentaBancaria(models.Model):
    TIPO_CUENTA = [
        ('AHORRO', 'AHORRO'),
        ('CORRIENTE', 'CORRIENTE'),
    ],
    TIPO_MONEDA = [
        ('USD', 'USD'),
        ('PEN', 'PEN'),
    ],
    intIdCuenta = models.AutoField(primary_key=True)
    intIdProveedor = models.AutoField(primary_key=True)
    strNroCuenta = models.CharField(max_length=50, null=True)
    strTipoCuenta = models.CharField(max_length=10, choices=TIPO_CUENTA, default='')
    strMoneda = models.CharField(max_length=50, null=True)
    strBeneficiario = models.CharField(max_length=250, null=True)
    strDescripcion = models.CharField(max_length=500, null=True)
    strUsuarioCrea = models.CharField(max_length=35, null=True)
    dtmFechaCrea = models.DateTimeField(auto_now_add=True)
    strUsuarioModif = models.CharField(max_length=35, null=True)
    dtmFechaModif = models.DateTimeField(auto_now=True)
    strEstado = models.CharField(max_length=1, null=True)

    class Meta:
        db_table = 'tblROpCuentaBancaria'
        verbose_name = 'ROpCuentaBancaria'
        verbose_name_plural = 'ROpCuentaBancaria'

    def __str__(self):
        return self.intIdProveedor


