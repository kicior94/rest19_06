# Generated by Django 3.2.4 on 2021-06-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='played',
            field=models.BooleanField(default=False),
        ),
    ]
