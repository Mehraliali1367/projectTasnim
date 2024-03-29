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

      # if not first_name:
        #     raise ValueError('کاربر باید نام داشته باشد')
        # if not last_name:
        #     raise ValueError('کاربر باید نام خانوادگی داشته باشد')
        # if not tel:
        #     raise ValueError('کاربر باید موبایل داشته باشد')
        # if not melli:
        #     raise ValueError('کد ملی صحیح نیست یا تکراری است')
class MyUserManager(BaseUserManager):
    def create_user(self, melli, serial,tel, first_name, last_name, year_brithday, password):
        user = self.model(melli=melli, serial=serial,tel=tel, first_name=first_name,
                          last_name=last_name, year_brithday=year_brithday)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, melli, serial,tel, first_name, last_name, password):
        user = self.create_user(melli=melli,serial=serial,tel=tel, first_name=first_name,
                                last_name=last_name, year_brithday=0000, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
