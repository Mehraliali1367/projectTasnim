from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User, Images
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('serial', 'melli', 'full_name', 'brithday', 'tel', 'place','date', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('اطلاعات کاربر', {'fields': ('serial', 'melli', 'full_name', 'brithday', 'tel', 'place','date', 'password')}),
        ('خصوصیات کاربر', {'fields': ('is_active',)}),
        ('سطح دسترسی', {'fields': ('is_admin',)})
    )
    add_fieldsets = (
        (None, {
            'fields': ('serial','melli', 'full_name', 'brithday', 'tel', 'place','date', 'password1', 'password2')
        }),
    )
    search_fields = ('serial',)
    ordering = ('full_name',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Images)
