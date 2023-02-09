from django.db import models
from account.models import User
from extensions.utils import jalali_converter
from django.utils import timezone


# class Evaluation(models.Model):
#     STATUS_CHOICES = (
#         ('a', 'کاملا راضی'),
#         ('b', 'راضی'),
#         ('c', 'ناراضی'),
#         ('d', 'کاملا ناراضی'),
#     )
#     STATUS_CHOICES2 = (
#         ('y', 'بله'),
#         ('n', 'خیر'),
#     )
#     clark = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="منشی")
#     s1 = models.CharField(
#         max_length=1, choices=STATUS_CHOICES, verbose_name='سوال1')
#     s2 = models.CharField(
#         max_length=1, choices=STATUS_CHOICES, verbose_name='سوال2')
#     s3 = models.CharField(
#         max_length=1, choices=STATUS_CHOICES, verbose_name='سوال3')
#     s4 = models.CharField(
#         max_length=1, choices=STATUS_CHOICES, verbose_name='سوال4')
#     s5 = models.CharField(
#         max_length=1, choices=STATUS_CHOICES, verbose_name='سوال5')
#     s6 = models.CharField(
#         max_length=1, choices=STATUS_CHOICES, verbose_name='سوال6')
#     s7 = models.CharField(
#         max_length=1, choices=STATUS_CHOICES, verbose_name='سوال7')
#     s8 = models.CharField(
#         max_length=1, choices=STATUS_CHOICES, verbose_name='سوال8')
#     s9 = models.CharField(
#         max_length=1, choices=STATUS_CHOICES, verbose_name='سوال9')
#     s10 = models.CharField(
#         max_length=1, choices=STATUS_CHOICES, verbose_name='سوال10')
#     s11 = models.CharField(
#         max_length=1, choices=STATUS_CHOICES, verbose_name='سوال11')
#     s12 = models.CharField(
#         max_length=1, choices=STATUS_CHOICES2, verbose_name='سوال12')
#     s13 = models.TextField(verbose_name="پیشنهادات")
#     date = models.DateTimeField(
#         default=timezone.now, verbose_name='تاریخ ایجاد')

#     def date_register(self):
#         return jalali_converter(self.date)


# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=500, null=True)
    op1 = models.CharField(max_length=200, null=True, verbose_name='گزینه 1')
    op2 = models.CharField(max_length=200, null=True, verbose_name='گزینه 2')
    op3 = models.CharField(max_length=200, null=True, verbose_name='گزینه 3')
    op4 = models.CharField(max_length=200, null=True, verbose_name='گزینه 4')
    date = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ایجاد')
    class Meta:
        verbose_name='سوال'
        verbose_name_plural='پرسش ها'
        ordering = ['-date']
    date = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.question

    def date_register(self):
        return jalali_converter(self.date)

class ResultModel(models.Model):
    question=models.ForeignKey(QuesModel,on_delete=models.CASCADE,related_name='results',verbose_name='سوال')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='results',verbose_name='پاسخ دهنده')
    ans=models.CharField(max_length=200,null=True,verbose_name='گزینه انتخاب شده')
    date = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ایجاد')
    
    class Meta:
        verbose_name='پاسخ'
        verbose_name_plural='پاسخ ها'
        ordering = ['-date']
        
    def __str__(self):
        return self.question.question

    def date_register(self):
        return jalali_converter(self.date)