# Generated by Django 3.2.8 on 2021-11-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionBD', '0024_auto_20211126_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='redireccion_cancion',
            field=models.CharField(max_length=30),
        ),
    ]