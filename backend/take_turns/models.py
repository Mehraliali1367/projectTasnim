from django.db import models
from account.models import User
from django.utils import timezone

class Services(models.Model):
    parent=models.ForeignKey('self',default=None,null=True,blank=True,on_delete=models.SET_NULL,related_name='children',verbose_name='زیردسته')
    service=models.CharField(max_length=120,verbose_name='نام دسته')
    date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='خدمت'
        verbose_name_plural='خدمات'
        ordering = ['-date']
 
    
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True, blank=True, null=True)
    category=models.ForeignKey(Services,on_delete=models.CASCADE,verbose_name="گروه کاری")
    date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='دکتر'
        verbose_name_plural='دکترها'
        ordering = ['-date']

class Presence(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='pdoctor')
    datetime_persian = models.CharField(max_length=10)
    from_hour = models.IntegerField()
    to_hour = models.IntegerField()
    interval_sick = models.IntegerField()
    date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name='حضور دکتر'
        verbose_name_plural='تاریخ و ساعت حضور دکتر'
        ordering = ['-date']
            
    def __str__(self):
        return self.doctor.name
    
# class payment(models.Model):
#     user=models.ForeignKey("User", verbose_name=_("نام کاربر"), on_delete=models.SET_NULL)
#     mony=models.DecimalField(null=True,blank=True,verbose_name='مبلغ تراکنش')
#     date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')
#     serial1=models.IntegerField(null=True,blank=True)
    
class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visit')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='vdoctor')
    datetime_persian = models.CharField(max_length=10)
    hour = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')
    reason = models.CharField(max_length=1000)
    category=models.ForeignKey(Services,on_delete=models.CASCADE,verbose_name="گروه مراجعه")
    date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')
   
    class Meta:
        verbose_name='نوبت'
        verbose_name_plural='لیست نوبت ها'
        ordering = ['-date']
    
    def __str__(self):
        return self.user.last_name


 