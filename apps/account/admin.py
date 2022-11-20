from django.contrib import admin
from django.contrib.auth.models import Group

from apps.account.models import User, BuyerUser, SellerUser, AdminUser
from apps.core.admin import AbstractBaseAdmin

admin.site.unregister(Group)


class AbstractUserAdmin(AbstractBaseAdmin):
    default_list_display = ('fullname', 'mobile_number', 'created_at')

    def fullname(self, obj):
        return f'{obj.first_name} {obj.last_name}'


@admin.register(User)
class UserAdmin(AbstractUserAdmin):
    list_display = ('role',)
    list_filter = ('role',)


@admin.register(BuyerUser)
class BuyerUserAdmin(AbstractUserAdmin):
    pass


@admin.register(SellerUser)
class SellerUserAdmin(AbstractUserAdmin):
    pass


@admin.register(AdminUser)
class AdminUserAdmin(AbstractUserAdmin):
    pass
