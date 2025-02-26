# Generated by Django 5.0.12 on 2025-02-11 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tblAcopiador',
            fields=[
                ('intAcopiadorId', models.AutoField(primary_key=True, serialize=False)),
                ('strRUC', models.CharField(max_length=20, null=True)),
                ('strAcopiador', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tblAcopiador',
            },
        ),
        migrations.CreateModel(
            name='tblEstado',
            fields=[
                ('intEstadoId', models.AutoField(primary_key=True, serialize=False)),
                ('strEstado', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tblEstado',
            },
        ),
        migrations.CreateModel(
            name='tblPesador',
            fields=[
                ('intPesadorId', models.AutoField(primary_key=True, serialize=False)),
                ('strNombres', models.CharField(max_length=255)),
                ('strApellidos', models.CharField(max_length=255)),
                ('strLogin', models.CharField(max_length=100)),
                ('strPwd', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tblPesador',
            },
        ),
        migrations.CreateModel(
            name='tblPlataforma',
            fields=[
                ('intPlataformaId', models.AutoField(primary_key=True, serialize=False)),
                ('strPlataforma', models.CharField(max_length=255)),
                ('intRUC', models.IntegerField(default=0)),
                ('strDireccion', models.CharField(max_length=255)),
                ('intSerieDocIdDefault', models.IntegerField(null=True)),
                ('intTarifaIdDefault', models.IntegerField(null=True)),
                ('blnRegistroDefault', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'tblPlataforma',
            },
        ),
        migrations.CreateModel(
            name='tblProcedencia',
            fields=[
                ('intProcedenciaId', models.AutoField(primary_key=True, serialize=False)),
                ('strProcedencia', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tblProcedencia',
            },
        ),
        migrations.CreateModel(
            name='tblProducto',
            fields=[
                ('intProductoId', models.AutoField(primary_key=True, serialize=False)),
                ('strProducto', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tblProducto',
            },
        ),
        migrations.CreateModel(
            name='tblSerieDoc',
            fields=[
                ('intSerieDocId', models.AutoField(primary_key=True, serialize=False)),
                ('strSerieDocAbrev', models.CharField(max_length=25)),
                ('strSerieDocDesc', models.CharField(max_length=50)),
                ('intCorrelActual', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'tblSerieDoc',
            },
        ),
        migrations.CreateModel(
            name='tblTarifa',
            fields=[
                ('intTarifaId', models.AutoField(primary_key=True, serialize=False)),
                ('strTarifa', models.CharField(max_length=40)),
                ('intNroEjes', models.IntegerField(null=True)),
                ('strMoneda', models.CharField(max_length=10)),
                ('intMonto', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tblTarifa',
            },
        ),
        migrations.CreateModel(
            name='tblTransportista',
            fields=[
                ('intTransportistaId', models.AutoField(primary_key=True, serialize=False)),
                ('intRUC', models.CharField(max_length=20, null=True)),
                ('strTransportista', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tblTransportista',
            },
        ),
        migrations.CreateModel(
            name='tblZona',
            fields=[
                ('intZonaId', models.AutoField(primary_key=True, serialize=False)),
                ('intCodigo', models.IntegerField(null=True)),
                ('strZona', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tblZona',
            },
        ),
        migrations.CreateModel(
            name='tblCliente',
            fields=[
                ('intClienteId', models.AutoField(primary_key=True, serialize=False)),
                ('strTipo', models.CharField(max_length=50)),
                ('strSubTipo', models.CharField(max_length=50)),
                ('intRUC', models.CharField(max_length=20, null=True)),
                ('strRazon', models.CharField(max_length=255)),
                ('strDireccion', models.CharField(max_length=255)),
                ('strTelefono', models.CharField(default=0, max_length=25)),
                ('fltFactorPeso', models.DecimalField(decimal_places=1, max_digits=2)),
                ('dtFechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('intPesadorModificacionId', models.IntegerField(null=True)),
                ('dtFechaModificacion', models.DateTimeField(auto_now=True)),
                ('intPesadorCreacionId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='balanza.tblpesador')),
            ],
            options={
                'db_table': 'tblCliente',
            },
        ),
        migrations.CreateModel(
            name='tblCertificado',
            fields=[
                ('intCertificadoId', models.AutoField(primary_key=True, serialize=False)),
                ('dtFechaIni', models.DateTimeField(auto_now_add=True)),
                ('dtFechaFin', models.DateField(auto_now=True)),
                ('intCertEstado', models.IntegerField(null=True)),
                ('fkPlataformald', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='balanza.tblplataforma')),
            ],
            options={
                'db_table': 'tblCertificado',
            },
        ),
        migrations.CreateModel(
            name='tblRecurrente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strRecurrenciaEstado', models.CharField(max_length=25)),
                ('intRecurrenteId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='balanza.tblcliente')),
            ],
            options={
                'db_table': 'tblRecurrente',
            },
        ),
        migrations.CreateModel(
            name='tblEntrada',
            fields=[
                ('intEntradaId', models.AutoField(primary_key=True, serialize=False)),
                ('strTipoMarca', models.CharField(max_length=50)),
                ('strPlaca1', models.CharField(max_length=25)),
                ('strPlaca2', models.CharField(max_length=25)),
                ('strConductor', models.CharField(max_length=50)),
                ('strNroGuia', models.CharField(max_length=50)),
                ('strNroGuiaT', models.CharField(max_length=50)),
                ('strPlaca', models.CharField(max_length=20)),
                ('intNroSacos', models.IntegerField(default=0)),
                ('strObservacion', models.CharField(max_length=150)),
                ('blnFlagRegulizar', models.BooleanField(default=False)),
                ('intPesoInicial', models.IntegerField(default=0)),
                ('blEliminado', models.BooleanField(default=False)),
                ('strEstacionPC', models.CharField(max_length=50)),
                ('dtFechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('dtFechaModificacion', models.DateTimeField(auto_now=True)),
                ('intAcopiadorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanza.tblacopiador')),
                ('intCertificadoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanza.tblcertificado')),
                ('intClienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanza.tblcliente')),
                ('intEstadoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanza.tblestado')),
                ('intPesadorCreacionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradasPesador_creadas', to='balanza.tblpesador')),
                ('intPesadorModificacionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradasPesador_modificadas', to='balanza.tblpesador')),
                ('intProcedenciaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanza.tblprocedencia')),
                ('intProductoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanza.tblproducto')),
                ('intRecurrenteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanza.tblrecurrente')),
                ('intSerieDocId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanza.tblseriedoc')),
                ('intTarifaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanza.tbltarifa')),
                ('intTransportistaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanza.tbltransportista')),
                ('intZonaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanza.tblzona')),
            ],
            options={
                'db_table': 'tblEntrada',
            },
        ),
        migrations.CreateModel(
            name='tblSalida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intPesoFinal', models.IntegerField(default=0)),
                ('dtFechaModificacion', models.DateTimeField(auto_now=True)),
                ('intEntrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanza.tblentrada')),
                ('intPesadorCreacionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salidasPesador_creadas', to='balanza.tblpesador')),
                ('intPesadorModificacionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salidasPesador_modificadas', to='balanza.tblpesador')),
            ],
            options={
                'db_table': 'tblSalida',
            },
        ),
    ]
