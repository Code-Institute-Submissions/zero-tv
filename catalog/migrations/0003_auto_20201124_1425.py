# Generated by Django 3.0.7 on 2020-11-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201124_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='minimum_age',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]