# Generated by Django 3.2.12 on 2022-11-16 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Price'),
        ),
    ]
