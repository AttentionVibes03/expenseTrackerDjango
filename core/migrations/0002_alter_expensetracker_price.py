# Generated by Django 4.2.6 on 2023-10-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensetracker',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
