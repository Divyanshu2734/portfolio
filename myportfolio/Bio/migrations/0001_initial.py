# Generated by Django 4.2.3 on 2023-08-15 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reachme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('discription', models.TextField()),
            ],
        ),
    ]