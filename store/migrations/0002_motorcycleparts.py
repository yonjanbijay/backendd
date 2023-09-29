# Generated by Django 4.2.3 on 2023-09-28 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='motorcycleParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motorcycle_partsname', models.CharField(max_length=25)),
                ('price1', models.IntegerField(default=0)),
                ('description1', models.CharField(max_length=50)),
                ('image1', models.ImageField(default='', upload_to='images/parts/')),
            ],
        ),
    ]
