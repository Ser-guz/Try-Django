# Generated by Django 2.2 on 2020-04-17 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200417_1726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-timestamp', '-updated']},
        ),
    ]
