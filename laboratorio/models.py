from django.db import models


class LeyesSur(models.Model):
    intIdLeyes = models.AutoField(primary_key=True)
    strTipoLey = models.CharField(max_length=30, null=True, blank=True)
    strTipoProceso = models.CharField(max_length=30, null=True, blank=True)
    strItem = models.CharField(max_length=30, null=True, blank=True)
    strBk = models.CharField(max_length=10, null=True, blank=True)
    dtmFecha = models.DateTimeField(null=True, blank=True)
    strTipoMineral = models.CharField(max_length=20, null=True, blank=True)
    strLote = models.CharField(max_length=20, null=True, blank=True)
    strPMFino = models.CharField(max_length=20, null=True, blank=True)
    strPMGrueso = models.CharField(max_length=20, null=True, blank=True)
    strPesoAuMasAg = models.CharField(max_length=20, null=True, blank=True)
    strPesoAuFino1 = models.CharField(max_length=20, null=True, blank=True)
    strPesoAuFino2 = models.CharField(max_length=20, null=True, blank=True)
    strPesoAuGrueso = models.CharField(max_length=20, null=True, blank=True)
    strLeyOzTcAuFino = models.CharField(max_length=20, null=True, blank=True)
    strLeyOzTcAuGrueso = models.CharField(max_length=20, null=True, blank=True)
    strLeyOzTcAuFinal = models.CharField(max_length=20, null=True, blank=True)
    strLeyOzTcAgfinal1 = models.CharField(max_length=20, null=True, blank=True)
    strLeyFinalAu = models.CharField(max_length=20, null=True, blank=True)
    strLeyFinalAg = models.CharField(max_length=20, null=True, blank=True)
    strPorcAuFino = models.CharField(max_length=20, null=True, blank=True)
    strPorcAuGrueso = models.CharField(max_length=20, null=True, blank=True)
    chrCheckStatus = models.CharField(max_length=1, null=True, blank=True)
    strUsuarioCrea = models.CharField(max_length=35, null=True, blank=True)
    dtmFechaCrea = models.DateTimeField(null=True, blank=True)
    strUsuarioModif = models.CharField(max_length=35, null=True, blank=True)
    dtmFechaModif = models.DateTimeField(null=True, blank=True)
    chrEstado = models.CharField(max_length=1, null=True, blank=True)

    class Meta:
        db_table = "LeyesSur"

    def __str__(self):
        return f"{self.intIdLeyes} - {self.strTipoLey}"
