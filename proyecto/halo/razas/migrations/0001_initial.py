# Generated by Django 3.1.3 on 2022-06-15 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('armas', models.TextField()),
                ('planeta', models.TextField()),
                ('papel', models.TextField()),
                ('rango', models.TextField()),
                ('habilidad', models.TextField()),
                ('tamaño', models.TextField()),
            ],
        ),
    ]
