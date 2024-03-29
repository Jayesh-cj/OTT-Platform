# Generated by Django 5.0.1 on 2024-03-29 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
        ('User', '0021_rename_from_user_tbl_chat_user_from'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_chatroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=200)),
                ('community_date', models.DateField()),
                ('community_photo', models.FileField(upload_to='Files/Community/Profile/')),
                ('community_description', models.TextField()),
                ('community_status', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.AddField(
            model_name='tbl_chat',
            name='room_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.tbl_chatroom'),
        ),
        migrations.CreateModel(
            name='tbl_joinlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_status', models.IntegerField(default=0)),
                ('community_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.tbl_chatroom')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
