# Generated by Django 4.2 on 2024-10-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category_post_notification_comment_bookmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.TextField(blank=True, null=True),
        ),
    ]
