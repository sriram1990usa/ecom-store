# Generated by Django 4.0.5 on 2022-07-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
