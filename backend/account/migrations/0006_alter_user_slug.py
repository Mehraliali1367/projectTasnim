# Generated by Django 4.1.7 on 2023-02-22 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, verbose_name='آدرس کاربر'),
        ),
    ]
