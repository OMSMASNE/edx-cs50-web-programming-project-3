# Generated by Django 2.0.3 on 2019-08-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190809_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='price',
            field=models.CharField(blank=True, default='0', max_length=10, null=True),
        ),
    ]
