# Generated by Django 4.2.3 on 2023-09-28 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_motorcycleparts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motorcycleparts',
            old_name='motorcycle_partsname',
            new_name='partName',
        ),
    ]
