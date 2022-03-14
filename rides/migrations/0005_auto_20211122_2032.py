# Generated by Django 3.2.8 on 2021-11-22 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0004_auto_20211122_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderticket',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='ride',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rides.ride'),
        ),
    ]
