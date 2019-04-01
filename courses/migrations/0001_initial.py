# Generated by Django 2.1.7 on 2019-04-01 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, max_length=120, unique=True)),
                ('category', models.ManyToManyField(to='courses.Category')),
            ],
        ),
    ]
