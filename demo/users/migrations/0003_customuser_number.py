# Generated by Django 4.0.1 on 2022-04-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_first_name_customuser_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='number',
            field=models.CharField(blank=True, max_length=250, verbose_name='Phone number'),
        ),
    ]
