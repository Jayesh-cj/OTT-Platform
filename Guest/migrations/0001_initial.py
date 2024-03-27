# Generated by Django 5.0.1 on 2024-02-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_contact', models.CharField(max_length=15)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_photo', models.FileField(upload_to='Files/User/Profile')),
                ('user_gender', models.CharField(max_length=50)),
                ('user_dob', models.DateField()),
                ('user_password', models.CharField(max_length=10)),
            ],
        ),
    ]
