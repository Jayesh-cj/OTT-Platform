# Generated by Django 5.0.1 on 2024-02-10 05:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_alter_tbl_trailer_trailer_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_crew',
            name='details_id',
        ),
        migrations.RemoveField(
            model_name='tbl_trailer',
            name='details_id',
        ),
        migrations.AddField(
            model_name='tbl_content_details',
            name='crew_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_crew'),
        ),
        migrations.AddField(
            model_name='tbl_content_details',
            name='trailer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_trailer'),
        ),
    ]
