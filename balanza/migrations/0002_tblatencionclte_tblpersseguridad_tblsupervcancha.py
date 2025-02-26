# Generated by Django 5.0.12 on 2025-02-12 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balanza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblAtencionClte',
            fields=[
                ('intAtencionClteId', models.AutoField(primary_key=True, serialize=False)),
                ('strPlaca', models.CharField(max_length=25)),
                ('fltPeso', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'tblAtencionClte',
            },
        ),
        migrations.CreateModel(
            name='tblPersSeguridad',
            fields=[
                ('intPersSeguridadId', models.AutoField(primary_key=True, serialize=False)),
                ('strNombreSeguridad', models.CharField(max_length=150)),
                ('strTipoMarca', models.CharField(max_length=50)),
                ('strPlaca', models.CharField(max_length=25)),
                ('strConductor', models.CharField(max_length=50)),
                ('dtmFechaIngreso', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'tblPersSeguridad',
            },
        ),
        migrations.CreateModel(
            name='tblSupervCancha',
            fields=[
                ('intSupervCanchaId', models.AutoField(primary_key=True, serialize=False)),
                ('strNombreSuperV', models.CharField(max_length=150)),
                ('strPlaca', models.CharField(max_length=25)),
                ('fltPeso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dtmFecha', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tblSupervCancha',
            },
        ),
    ]
