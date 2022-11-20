from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from apps.core.models import AbstractModel


class Inventory(AbstractModel):
    product = models.ForeignKey('apps.product.Product', on_delete=models.RESTRICT, verbose_name=_('Product'))
    quantity = models.IntegerField(verbose_name=_('Quantity'),
                                   null=True,
                                   blank=True
                                   )
    store_room = models.ForeignKey('apps.inventory.StoreRoom', on_delete=models.RESTRICT, verbose_name=_('Store Room'))
