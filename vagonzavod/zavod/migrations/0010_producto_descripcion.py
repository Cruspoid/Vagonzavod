# Generated by Django 4.0.4 on 2022-05-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavod', '0009_alter_producto_options_alter_producto_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default=1, max_length=200, verbose_name='descripcion'),
            preserve_default=False,
        ),
    ]
