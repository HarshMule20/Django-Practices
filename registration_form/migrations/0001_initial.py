# Generated by Django 3.0.8 on 2020-07-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('profile_photo', models.TextField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_no', models.CharField(max_length=10)),
                ('address_1', models.TextField()),
                ('address_2', models.TextField()),
                ('dob', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pin_code', models.CharField(max_length=10)),
            ],
        ),
    ]
