# Generated by Django 4.0.2 on 2022-02-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('urls', models.URLField(max_length=600)),
                ('description', models.TextField(max_length=5000)),
                ('category', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('client', models.CharField(max_length=100)),
                ('img_path', models.CharField(max_length=200)),
            ],
        ),
    ]