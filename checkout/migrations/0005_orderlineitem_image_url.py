# Generated by Django 3.1.13 on 2021-07-12 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_orderlineitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
