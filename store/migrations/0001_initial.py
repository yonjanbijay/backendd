# Generated by Django 4.2.3 on 2023-07-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='motorcycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motorcycle_model', models.CharField(max_length=25)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='images/')),
            ],
        ),
    ]