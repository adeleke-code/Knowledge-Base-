# Generated by Django 4.0 on 2023-02-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_config', '0005_adminpage_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='KB_Admin_logo'),
        ),
    ]
