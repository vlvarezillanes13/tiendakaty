# Generated by Django 3.2.5 on 2021-07-21 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_rename_product_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='anulate',
            new_name='anulado',
        ),
    ]
