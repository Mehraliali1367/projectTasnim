# Generated by Django 4.0.6 on 2023-01-16 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suggestions', '0003_alter_quesmodel_ans_op1_alter_quesmodel_ans_op2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quesmodel',
            name='ans_op1',
        ),
        migrations.RemoveField(
            model_name='quesmodel',
            name='ans_op2',
        ),
        migrations.RemoveField(
            model_name='quesmodel',
            name='ans_op3',
        ),
        migrations.RemoveField(
            model_name='quesmodel',
            name='ans_op4',
        ),
        migrations.CreateModel(
            name='ResultModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans_op1', models.BooleanField(null=True, verbose_name='انتخاب گزینه op1')),
                ('ans_op2', models.BooleanField(null=True, verbose_name='انتخاب گزینه op2')),
                ('ans_op3', models.BooleanField(null=True, verbose_name='انتخاب گزینه op3')),
                ('ans_op4', models.BooleanField(null=True, verbose_name='انتخاب گزینه op4')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ایجاد')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='suggestions.quesmodel', verbose_name='سوال')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to=settings.AUTH_USER_MODEL, verbose_name='پاسخ دهنده')),
            ],
        ),
    ]
