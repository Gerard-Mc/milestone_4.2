# Generated by Django 3.1.13 on 2021-07-17 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0016_auto_20210717_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='grand_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
        ),
    ]