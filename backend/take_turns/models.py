from django.db import models
from account.models import User
from django.utils import timezone


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Presence(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='pdoctor')
    datetime_persian = models.CharField(max_length=10)
    from_hour = models.IntegerField()
    to_hour = models.IntegerField()
    interval_sick = models.IntegerField()

    def __str__(self):
        return self.doctor.name


class Visit(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='vdoctor')
    datetime_persian = models.CharField(max_length=10)
    hour = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visit')
    reason = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.full_name


class Services(models.Model):
    service = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')
