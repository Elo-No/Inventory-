from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .enums import UserRole
from .managers import UserManager, BuyerManager, SellerManager, AdminManager
from apps.core.models import AbstractModel
from apps.core.validator import UnicodeMobileNumberValidator


class User(AbstractBaseUser, AbstractModel):
    mobile_number_validator = UnicodeMobileNumberValidator()
    first_name = models.CharField(max_length=64, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=64, verbose_name=_('Last Name'))
    mobile_number = models.CharField(max_length=32, unique=True, db_index=True, verbose_name=_('Mobile Number'))
    role = models.IntegerField(default=UserRole.BUYER, choices=UserRole.choices, db_index=True, verbose_name=_('Role'))

    is_superuser = models.BooleanField(default=False, verbose_name=_('Is super user'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Is staff'))

    objects = UserManager()
    USERNAME_FIELD = 'mobile_number'

    # For checking permissions. to keep it simple all admin have ALL permissons

    def has_perm(self, perm, obj=None):
        return self.is_staff or self.is_superuser

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BuyerUser(User):
    objects = BuyerManager

    class Meta:
        proxy = True


class SellerUser(User):
    objects = SellerManager

    class Meta:
        proxy = True


class AdminUser(User):
    objects = AdminManager

    class Meta:
        proxy = True
