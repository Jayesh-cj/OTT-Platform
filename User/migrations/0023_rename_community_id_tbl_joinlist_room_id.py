# Generated by Django 5.0.1 on 2024-04-08 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0022_tbl_chatroom_tbl_chat_room_id_tbl_joinlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_joinlist',
            old_name='community_id',
            new_name='room_id',
        ),
    ]
