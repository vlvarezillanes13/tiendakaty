# Generated by Django 3.2.5 on 2021-07-28 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0008_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together={('nombre', 'marca')},
        ),
    ]
