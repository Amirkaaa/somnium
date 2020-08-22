from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from group.models import Group
from profession.models import Profession


# Create your models here.
class Position(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='positions')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='positions')
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name='positions')
    salary = models.PositiveIntegerField(_('Зарплата'))

    def __str__(self):
        return '{} {} {}'.format(self.user, self.group, self.profession)

    class Meta:
        verbose_name = _('Должность')
        verbose_name_plural = _('Должности')
