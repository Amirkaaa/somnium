from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Group(models.Model):
    name = models.CharField(_('Название'), max_length=64)
    director = models.ForeignKey('Group', verbose_name=_('Начальство'), null=True, blank=True, on_delete=models.CASCADE,
                                 help_text=_('Выше стоящее руководство'), related_name='branches')

    def __str__(self):
        return '{} - {}'.format(self.name, self.director)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
