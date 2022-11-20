from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Modified at')
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Is deleted ?'),
    )
    is_archived = models.BooleanField(
        default=False,
        verbose_name=_('Is archived ?'),
    )

    class Meta:
        abstract = True
