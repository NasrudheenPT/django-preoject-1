# Generated by Django 3.1.6 on 2021-02-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='student name')),
                ('age', models.IntegerField(default=0, verbose_name='Age')),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
