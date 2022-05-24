# Generated by Django 4.0.4 on 2022-05-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_alter_news_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialsidebar',
            name='background',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='socialsidebar',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='news/'),
        ),
        migrations.AddField(
            model_name='socialsidebar',
            name='social_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='socialsidebar',
            name='link_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
