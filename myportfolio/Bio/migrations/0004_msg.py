# Generated by Django 4.2.3 on 2023-08-17 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bio', '0003_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=90)),
                ('subject', models.TextField()),
                ('mssages', models.TextField()),
            ],
        ),
    ]
