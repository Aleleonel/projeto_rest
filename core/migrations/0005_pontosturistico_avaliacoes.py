# Generated by Django 3.0.5 on 2020-04-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('core', '0004_pontosturistico_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturistico',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.Avaliacao'),
        ),
    ]
