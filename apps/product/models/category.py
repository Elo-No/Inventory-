from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import AbstractModel


class Category(AbstractModel):
    title = models.CharField(
        verbose_name=_('Name'),
        max_length=64,
        null=True,
        blank=True
    )
