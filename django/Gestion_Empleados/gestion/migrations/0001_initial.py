# Generated by Django 5.0.2 on 2024-03-23 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pais', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('nombre_puesto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Salario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_bruto_año', models.IntegerField()),
                ('extra_junio', models.BooleanField()),
                ('extra_diciembre', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Poblacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_poblacion', models.CharField(max_length=60)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestion.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Fabrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fabrica', models.CharField(max_length=50)),
                ('direccion_fabrica', models.CharField(max_length=40)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('poblacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestion.poblacion')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empleado', models.CharField(max_length=50)),
                ('documento', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=75)),
                ('direccion_empleado', models.CharField(max_length=40)),
                ('fabrica', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestion.fabrica')),
                ('puesto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestion.puesto')),
            ],
        ),
        migrations.AddField(
            model_name='puesto',
            name='salario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestion.salario'),
        ),
    ]
