# Generated by Django 5.0.1 on 2024-02-10 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_remove_tbl_content_details_crew_id_delete_tbl_crew'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_content_details',
            name='trailer_id',
        ),
        migrations.AddField(
            model_name='tbl_trailer',
            name='details_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_content_details'),
        ),
    ]
