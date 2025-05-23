# Generated by Django 5.1.7 on 2025-04-07 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0002_empresa_trabajador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='identificador',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='trabajador',
            name='fecha_nacimiento',
        ),
        migrations.AddField(
            model_name='equipo',
            name='mac',
            field=models.CharField(default='00:11:22:33:44:55', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='marca',
            field=models.CharField(default='Sin marca', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(default='Equipo sin nombre', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trabajador',
            name='fecha_nacim',
            field=models.DateField(default='00:00:00:00:00:00'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='red',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='miApp.red'),
        ),
        migrations.AlterField(
            model_name='red',
            name='fecha_creacion',
            field=models.DateTimeField(default='Fecha creacion'),
        ),
        migrations.AlterField(
            model_name='red',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trabajadores', to='miApp.empresa'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
