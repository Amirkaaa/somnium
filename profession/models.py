from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Profession(models.Model):
    name = models.CharField(_('Название'), max_length=32)
    code = models.CharField(_('Код'), max_length=4, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.code)

    class Meta:
        verbose_name = _('Профессия')
        verbose_name_plural = _('Профессии')
