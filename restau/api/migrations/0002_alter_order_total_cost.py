# Generated by Django 4.2.7 on 2023-11-05 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
