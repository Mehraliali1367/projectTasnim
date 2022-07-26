# Generated by Django 4.0.6 on 2022-09-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-date'], 'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربران'},
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='نام '),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=500, verbose_name='نام خانوادگی'),
        ),
    ]
