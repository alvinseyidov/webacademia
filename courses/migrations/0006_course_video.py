# Generated by Django 2.1.7 on 2019-04-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20190402_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]
