# Generated by Django 4.0.3 on 2022-03-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]