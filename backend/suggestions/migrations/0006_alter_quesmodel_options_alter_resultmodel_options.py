# Generated by Django 4.0.6 on 2023-02-07 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0005_remove_resultmodel_ans_op1_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quesmodel',
            options={'ordering': ['-date'], 'verbose_name': 'سوال', 'verbose_name_plural': 'پرسش ها'},
        ),
        migrations.AlterModelOptions(
            name='resultmodel',
            options={'ordering': ['-date'], 'verbose_name': 'پاسخ', 'verbose_name_plural': 'پاسخ ها'},
        ),
    ]