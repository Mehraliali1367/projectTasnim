# Generated by Django 4.0.6 on 2023-01-15 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0002_quesmodel_ans_op1_quesmodel_ans_op2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quesmodel',
            name='ans_op1',
            field=models.IntegerField(default=0, null=True, verbose_name='تعدادانتخاب گزینه op1'),
        ),
        migrations.AlterField(
            model_name='quesmodel',
            name='ans_op2',
            field=models.IntegerField(default=0, null=True, verbose_name='تعدادانتخاب گزینه op2'),
        ),
        migrations.AlterField(
            model_name='quesmodel',
            name='ans_op3',
            field=models.IntegerField(default=0, null=True, verbose_name='تعدادانتخاب گزینه op3'),
        ),
        migrations.AlterField(
            model_name='quesmodel',
            name='ans_op4',
            field=models.IntegerField(default=0, null=True, verbose_name='تعدادانتخاب گزینه op4'),
        ),
    ]
