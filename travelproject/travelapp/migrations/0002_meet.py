# Generated by Django 4.1 on 2024-03-22 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('img1', models.ImageField(upload_to='gallery')),
                ('desc1', models.TextField()),
            ],
        ),
    ]
