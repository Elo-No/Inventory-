from django.db import models

from apps.account.enums import UserRole


class BuyerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=UserRole.BUYER)


class SellerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=UserRole.BUYER)


class AdminManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=UserRole.BUYER)


class UserManager(models.Manager):
    use_in_migrations = True

    def _create_user(self, mobile_number, password, **extra_fields):
        if not mobile_number:
            raise ValueError('The given username must be set')
        mobile_number = self.normalize_mobile_number(mobile_number)
        user = self.model(mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_buyer(self, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', UserRole.BUYER)
        return self._create_user(mobile_number, password, **extra_fields)

    def create_admin(self, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', UserRole.ADMIN)
        return self._create_user(mobile_number, password, **extra_fields)

    def create_seller(self, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', UserRole.SELLER)
        return self._create_user(mobile_number, password, **extra_fields)

    def create_superuser(self, mobile_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', UserRole.ADMIN)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(mobile_number, password, **extra_fields)

    def normalize_mobile_number(self, mobile_number):
        if isinstance(mobile_number, int):
            mobile_number = f'0{mobile_number}'
        if isinstance(mobile_number, str):
            if mobile_number.startswith('+98'):
                mobile_number = mobile_number.replace('+98', '0')
        return mobile_number

    def get_by_natural_key(self, mobile_number):
        return self.get(**{self.model.USERNAME_FIELD: mobile_number})
