from rest_framework import serializers
from .models import tblSupervCancha


class tblSupervCanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblSupervCancha
        fields = ['intSupervCanchaId', 'strNombreSuperV', 'strPlaca', 'fltPeso']
