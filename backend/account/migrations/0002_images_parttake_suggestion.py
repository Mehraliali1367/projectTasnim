# Generated by Django 4.1.7 on 2023-02-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='parttake_suggestion',
            field=models.BooleanField(blank=True, null=True, verbose_name='شرکت در نظرسنجی'),
        ),
    ]
