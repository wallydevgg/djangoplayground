from rest_framework import serializers
from .models import tblSupervCancha, tblPersSeguridad


class tblSupervCanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblSupervCancha
        fields = ["intSupervCanchaId", "strNombreSuperV", "strPlaca", "fltPeso"]


class tblPersSeguridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblPersSeguridad
        fields = [
            "intPersSeguridadId",
            "strNombreSeguridad",
            "strTipoMarca",
            "strPlaca",
            "strConductor",
        ]
