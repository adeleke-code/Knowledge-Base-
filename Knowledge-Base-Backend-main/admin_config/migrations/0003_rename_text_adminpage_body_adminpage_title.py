# Generated by Django 4.0 on 2023-02-23 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_config', '0002_alter_adminpage_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminpage',
            old_name='text',
            new_name='body',
        ),
        migrations.AddField(
            model_name='adminpage',
            name='title',
            field=models.CharField(max_length=350, null=True),
        ),
    ]
