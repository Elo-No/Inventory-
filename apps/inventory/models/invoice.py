from django.db import models

from apps.core.models import AbstractModel
from apps.inventory.models import Inventory


class Invoice(AbstractModel):
    sore_room = models.ForeignKey('apps.inventory.StoreRoom', on_delete=models.RESTRICT)
    price = models.DecimalField(max_digits=30, decimal_places=2, editable=False)


class InvoiceDetails(AbstractModel):
    product = models.ForeignKey('apps.inventory.Product', on_delete=models.RESTRICT, editable=False)
    quantity = models.IntegerField(default=1, editable=False)
    invoice = models.ForeignKey('apps.inventory.Invoice', on_delete=models.RESTRICT, editable=False)
    price = models.DecimalField(max_digits=25, decimal_places=2, editable=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.price = self.quantity * Inventory.objects.filter(product=self.product,
                                                              store_room=self.invoice.sore_room).first() or 0
        super(InvoiceDetails, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
