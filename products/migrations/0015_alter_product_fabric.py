# Generated by Django 4.2.7 on 2024-05-23 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20231111_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fabric',
            field=models.TextField(),
        ),
    ]
