# Generated by Django 2.1.7 on 2019-04-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_videos_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='duration',
            field=models.DurationField(help_text='duration', null=True),
        ),
    ]
