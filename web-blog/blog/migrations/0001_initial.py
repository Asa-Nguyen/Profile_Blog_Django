# Generated by Django 4.2.3 on 2023-07-08 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
