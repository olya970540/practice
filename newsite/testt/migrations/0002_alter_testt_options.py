# Generated by Django 3.2.5 on 2021-07-21 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testt', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testt',
            options={'ordering': ['-created_at'], 'verbose_name': 'New', 'verbose_name_plural': 'News'},
        ),
    ]
