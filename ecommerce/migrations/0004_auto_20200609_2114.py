# Generated by Django 3.0.6 on 2020-06-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20200609_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='permission',
            field=models.ManyToManyField(to='ecommerce.Permission'),
        ),
    ]
