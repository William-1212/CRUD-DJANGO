# Generated by Django 3.1.5 on 2021-01-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='materias',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('esporte', models.CharField(max_length=255)),
            ],
        ),
    ]
