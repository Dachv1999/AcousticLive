# Generated by Django 3.2.8 on 2021-10-21 04:04

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('gestionBD', '0002_leccion_idprofesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leccion',
            name='idprofesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionBD.profesor'),
        ),
    ]
