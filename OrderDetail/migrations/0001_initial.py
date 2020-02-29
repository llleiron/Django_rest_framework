# Generated by Django 2.0.12 on 2020-02-29 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Order', '0001_initial'),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.CharField(max_length=10, verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Product')),
            ],
        ),
    ]
