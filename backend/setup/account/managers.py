from django.contrib.auth.models import BaseUserManager
from django.db import models


def serial_auto():
    try:
        obj = models.User.objects.all().order_by('Id').last()
        if not obj:
            return 1
        else:
            return obj.slug + 1
    except:
        return 1


class MyUserManager(BaseUserManager):
    def create_user(self, serial, full_name, tel, password):
        if not serial:
            serial = serial_auto()
        if not full_name:
            raise ValueError('کاربر باید نام داشته باشد')
        if not tel:
            raise ValueError('کاربر باید موبایل داشته باشد')
        user = self.model(serial=serial, full_name=full_name, tel=tel)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, serial, full_name, tel, password):
        user = self.create_user(serial, full_name, tel, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

