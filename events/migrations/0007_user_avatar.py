# Generated by Django 5.2 on 2025-04-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_remove_event_event_date_event_event_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='User-icon.png', upload_to=''),
        ),
    ]
