from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class UserRole(IntegerChoices):
    ADMIN = 0, _('Admin')
    SELLER = 1, _('Seller')
    BUYER = 2, _('Buyer')
