# Generated by Django 4.2.6 on 2023-10-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Player_Name', models.CharField(max_length=50)),
                ('Jersy_No', models.IntegerField()),
                ('Team', models.CharField(max_length=20)),
                ('Goals', models.IntegerField()),
                ('Position', models.CharField(max_length=100)),
            ],
        ),
    ]
