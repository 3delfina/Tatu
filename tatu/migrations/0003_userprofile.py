# Generated by Django 2.0.3 on 2018-03-13 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatu', '0002_auto_20180313_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('workplace', models.CharField(blank=True, max_length=100)),
                ('phone_no', models.IntegerField(blank=True, max_length=30)),
                ('website', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
