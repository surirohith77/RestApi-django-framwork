# Generated by Django 5.0.7 on 2024-07-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0003_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
