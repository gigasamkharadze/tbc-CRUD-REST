from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Product(models.Model):
    categories = models.ManyToManyField('Category', related_name='products', verbose_name=_('Categories'))
    title = models.CharField(max_length=120, verbose_name=_('Title'))
    price = models.DecimalField(decimal_places=2, max_digits=10000, verbose_name=_('Price'))
    amount = models.IntegerField(verbose_name=_('Amount'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['price', 'amount']


class Category(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('Title'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['title']
