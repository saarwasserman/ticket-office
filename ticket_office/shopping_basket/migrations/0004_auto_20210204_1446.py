# Generated by Django 3.1.5 on 2021-02-04 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_catalog', '0004_auto_20210204_1427'),
        ('shopping_basket', '0003_auto_20210204_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketline',
            name='price',
        ),
        migrations.AlterField(
            model_name='basketline',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basket_lines', to='event_catalog.event'),
        ),
    ]
