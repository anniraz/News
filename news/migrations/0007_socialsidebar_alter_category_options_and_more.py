# Generated by Django 4.0.4 on 2022-05-09 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialSidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_address', models.CharField(help_text='ссылка на ресурс, например ссылка на инстаграм: https://www.instagram.com/mbcstudio_org/', max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Новости'},
        ),
    ]