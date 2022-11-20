# Generated by Django 3.2.12 on 2022-11-16 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20221115_2110'),
        ('product', '0005_alter_product_price'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='product.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='store_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.storeroom', verbose_name='Store Room'),
        ),
        migrations.AlterField(
            model_name='storeroom',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='storeroom',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='storeroom',
            name='seller',
            field=models.ManyToManyField(to='account.SellerUser', verbose_name='Seller'),
        ),
    ]
