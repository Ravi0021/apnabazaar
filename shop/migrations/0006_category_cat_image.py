# Generated by Django 3.0.5 on 2020-05-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200414_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, default='', upload_to='shop/images/category'),
        ),
    ]
