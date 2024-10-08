# Generated by Django 5.0.7 on 2024-08-01 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=128)),
                ('dirección', models.CharField(max_length=255)),
                ('dirección2', models.CharField(blank=True, max_length=255)),
                ('ciudad', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('código_postal', models.CharField(max_length=20)),
            ],
        ),
    ]
