# Generated by Django 4.2.7 on 2023-12-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='email',
            field=models.TextField(max_length=122),
        ),
    ]
