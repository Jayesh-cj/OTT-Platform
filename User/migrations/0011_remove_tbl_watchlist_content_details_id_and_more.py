# Generated by Django 5.0.1 on 2024-03-10 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_alter_tbl_complaint_complaint_replay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_watchlist_content',
            name='details_id',
        ),
        migrations.RemoveField(
            model_name='tbl_watchlist_content',
            name='watchlist_id',
        ),
        migrations.DeleteModel(
            name='tbl_review',
        ),
        migrations.DeleteModel(
            name='tbL_watchlist_content',
        ),
    ]
