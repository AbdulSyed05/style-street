# Generated by Django 4.2.7 on 2023-10-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_category_cat_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
