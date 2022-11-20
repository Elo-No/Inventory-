from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import AbstractModel


class Product(AbstractModel):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=64,
        null=True,
        blank=True
    )
    category = models.ForeignKey('apps.product.category', on_delete=models.RESTRICT, verbose_name=_('Category'))
    price = models.DecimalField(verbose_name=_('Price'), max_digits=20, decimal_places=2, null=True, blank=True)
