# Generated by Django 4.2.6 on 2023-10-20 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('date', models.DateField()),
            ],
        ),
    ]
