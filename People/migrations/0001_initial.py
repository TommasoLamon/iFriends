# Generated by Django 3.2.5 on 2021-11-19 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('headshot', models.ImageField(blank=True, upload_to='img')),
                ('text', models.TextField(blank=True, max_length=500, verbose_name='Desc')),
            ],
        ),
    ]
