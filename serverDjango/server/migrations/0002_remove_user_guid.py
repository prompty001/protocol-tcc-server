# Generated by Django 4.2.3 on 2023-07-04 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='guid',
        ),
    ]