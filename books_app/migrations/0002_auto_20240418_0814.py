from __future__ import unicode_literals

from django.core.management import call_command
from django.db import migrations


def load_data(apps, schema_editor):
    call_command('loaddata', 'test_data.json')


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0001_initial'),
    ]

    operations = [migrations.RunPython(load_data)]