from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User, Images
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('melli', 'last_name', 'first_name', 'year_brithday','slug','serial',
                    'tel', 'place', 'date_register', 'is_active','is_admin', 'is_reception')
    list_filter = ('is_admin', 'is_reception', 'place','date')
    fieldsets = (
        ('اطلاعات کاربر', {'fields': ('melli', 'last_name','slug','serial',
         'first_name', 'year_brithday', 'tel', 'place', 'date', 'password')}),
        ('خصوصیات کاربر', {'fields': ('is_active',)}),
        ('سطح دسترسی', {'fields': ('is_admin', 'is_reception')})
    )
    add_fieldsets = (
        (None, {
            'fields': ('melli', 'last_name', 'first_name', 'year_brithday', 'tel', 'place', 'date', 'password1', 'password2')
        }),
    )
    search_fields = ('is_reception', 'is_admin','date')
    ordering = ('-date',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Images)
