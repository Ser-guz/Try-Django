# Generated by Django 2.2 on 2020-04-19 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20200419_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchquery',
            name='query',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
