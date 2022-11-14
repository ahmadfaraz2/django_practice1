# Generated by Django 3.2.5 on 2022-11-14 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('permalink', models.CharField(max_length=40, unique=True)),
                ('update_date', models.DateTimeField(verbose_name='Last Updated')),
                ('bodytext', models.TextField(blank=True, verbose_name='Page Content')),
            ],
        ),
    ]
