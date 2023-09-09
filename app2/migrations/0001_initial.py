# Generated by Django 4.0.2 on 2023-09-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]
