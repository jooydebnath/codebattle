# Generated by Django 4.1.3 on 2022-11-01 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_user_facebook_user_github_user_linkedin_user_twitter_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-end_date']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['avatar']},
        ),
    ]
