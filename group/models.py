from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Group(models.Model):
    name = models.CharField(_('Название'), max_length=64)
    director = models.ForeignKey('Group', on_delete=models.CASCADE, help_text=_('Начальство'), related_name='branches')
