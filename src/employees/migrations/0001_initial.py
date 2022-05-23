# Generated by Django 4.0.4 on 2022-05-20 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('last_name', models.CharField(blank=True, default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]