# Generated by Django 4.0.1 on 2022-05-16 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_estate_address_alter_estate_bathroom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Category'),
        ),
    ]
