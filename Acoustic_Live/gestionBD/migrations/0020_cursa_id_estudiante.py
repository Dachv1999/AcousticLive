# Generated by Django 3.2.8 on 2021-11-18 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionBD', '0019_cursa_nivel_leccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursa',
            name='id_estudiante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionBD.estudiante'),
        ),
    ]
