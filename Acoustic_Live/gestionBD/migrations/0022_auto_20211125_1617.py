# Generated by Django 3.2.8 on 2021-11-25 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionBD', '0021_cancion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='genero_musica',
            field=models.CharField(default='f', max_length=100),
        ),
        migrations.AlterField(
            model_name='cancion',
            name='grupo_artista',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='cancion',
            name='imagen_cancion',
            field=models.ImageField(blank=True, default='', upload_to='static/Imagenes/imagenes_canciones'),
        ),
    ]