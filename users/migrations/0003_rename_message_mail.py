# Generated by Django 3.2.5 on 2021-07-14 00:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Mail',
        ),
    ]