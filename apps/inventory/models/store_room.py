from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import AbstractModel


class StoreRoom(AbstractModel):
    name = models.CharField(verbose_name=_('Name'),
                            max_length=64,
                            null=True,
                            blank=True
                            )
    address = models.TextField(verbose_name=_('Address'),
                               null=True, blank=True)
    seller = models.ManyToManyField('apps.account.SellerUser', verbose_name=_('Seller'))

    def __str__(self):
        return f'{self.name} {self.seller}'
