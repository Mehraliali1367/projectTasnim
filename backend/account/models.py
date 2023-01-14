import jdatetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from . import managers
from django.dispatch import receiver  # add this
from django.db.models.signals import post_save  # add this
from kavenegar import *
from django.utils import timezone
from extensions.utils import jalali_converter


class User(AbstractUser):
    serial = models.CharField(
        max_length=20, primary_key=True, unique=True, verbose_name='سریال')
    melli = models.CharField(max_length=10, blank=True,
                             null=True, verbose_name='کدملی')
    username = models.CharField(max_length=10, blank=True, null=True)
    full_name = models.CharField(max_length=500, verbose_name='نام خانوادگی')
    name = models.CharField(max_length=500, blank=True,
                            null=True, verbose_name='نام ')
    brithday = models.IntegerField(verbose_name='سن', blank=True, null=True)
    place = models.CharField(
        max_length=500, verbose_name='محل سکونت', blank=True, null=True)
    tel = models.CharField(max_length=20, verbose_name='موبایل')
    date = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ عضویت')
    is_admin = models.BooleanField(default=False, verbose_name='کاربر ارشد')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_reception = models.BooleanField(
        default=False, blank=True, null=True, verbose_name='پذیرش')
    objects = managers.MyUserManager()
    USERNAME_FIELD = 'serial'
    REQUIRED_FIELDS = ('full_name', 'tel')

    def __str__(self):
        return self.serial

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def date_register(self):
        return jalali_converter(self.date)

    date_register.short_description = "تاریخ عضویت"

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        ordering = ['-date']


class Images(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(default='1.jpg')
    objects = models.Manager()

    # @receiver(post_save, sender=User)  # add this
    # def create_user_images(sender, instance, created, **kwargs):
    #     if created:
    #         Images.objects.create(user=instance)

    def __str__(self):
        return self.user.serial


def save_images(sender, **kwargs):
    user = User.objects.get(serial=kwargs['instance'])
    if kwargs['created']:
        try:
            import json
        except ImportError:
            import simplejson as json
        try:
            api = KavenegarAPI(
                '4C6A7A6F556F6A68766F444466794278494C3738383433727239755636732B4831786E2B7653516C376C493D')
            params = {
                'receptor': user.tel,
                'token': user.serial,
                'token2': user.serial,
                'template': 'tasnim1'
            }
            response = api.verify_lookup(params)
            if response:
                pass
        except APIException:
            pass


post_save.connect(save_images, sender=Images)
