# Generated by Django 3.2.6 on 2021-08-20 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_nri_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nri',
            name='details',
            field=models.CharField(max_length=200),
        ),
    ]