# Generated by Django 2.1.7 on 2019-04-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_videos_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]