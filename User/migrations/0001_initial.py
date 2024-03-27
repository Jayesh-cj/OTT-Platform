# Generated by Django 5.0.1 on 2024-02-08 07:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=200)),
                ('community_date', models.DateField()),
                ('community_photo', models.FileField(upload_to='')),
                ('community_description', models.TextField()),
                ('community_status', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_content', models.TextField()),
                ('chat_date', models.DateField()),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
                ('community_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.tbl_community')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_community_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmp_community_title', models.CharField(max_length=200)),
                ('cmp_community_content', models.TextField()),
                ('cmp_community_date', models.DateField()),
                ('cmp_community_status', models.IntegerField(default=0)),
                ('cmp_community_replay', models.TextField()),
                ('community_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.tbl_community')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=200)),
                ('complaint_content', models.TextField()),
                ('complaint_date', models.DateField()),
                ('complaint_status', models.IntegerField(default=0)),
                ('complaint_replay', models.TextField()),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_content', models.TextField()),
                ('feedback_date', models.DateField()),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_joinlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_status', models.IntegerField(default=0)),
                ('community_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.tbl_community')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_rating', models.IntegerField()),
                ('review_content', models.TextField()),
                ('review_date', models.DateField()),
                ('details_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_content_details')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_date', models.DateField()),
                ('subscription_status', models.IntegerField(default=0)),
                ('package_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_package')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watchlist_name', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbL_watchlist_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wlist_date', models.DateField()),
                ('details_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_content_details')),
                ('watchlist_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.tbl_watchlist')),
            ],
        ),
    ]
