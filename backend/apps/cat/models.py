from ai_django_core.models import CommonInfo
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.account.models import EmailUser
from apps.cat.managers import CatQuerySet


class Food(models.Model):
    name = models.CharField(_('Name'), max_length=50)

    class Meta:
        verbose_name = _('Nahrung')
        verbose_name_plural = _('Nahrung')

    def __str__(self):
        return self.name


class Hideout(models.Model):
    name = models.CharField(_('Name'), max_length=50)

    class Meta:
        verbose_name = _('Versteck')
        verbose_name_plural = _('Verstecke')

    def __str__(self):
        return self.name


class Cat(CommonInfo):
    class ColourChoices(models.IntegerChoices):
        WHITE = 1, _('Weiß')
        BLACK = 2, _('Schwarz')
        TABBY = 3, _('Getigert')

    name = models.CharField(_('Name'), max_length=50)
    owner = models.ForeignKey(EmailUser, verbose_name=_('Besitzer'), related_name='cats', on_delete=models.CASCADE)
    current_hideout = models.ForeignKey(Hideout, verbose_name=_('Aktuelles Versteck'), related_name='cats',
                                        null=True, blank=True, on_delete=models.SET_NULL)
    favourite_foods = models.ManyToManyField(Food, verbose_name=_('Lieblingsessen'), related_name='cats')
    colour = models.PositiveSmallIntegerField(_('Farbe'), choices=ColourChoices.choices, default=ColourChoices.TABBY)
    age = models.PositiveIntegerField(_('Alter'), default=7)
    last_time_petted = models.DateTimeField(_('Letztes Mal gestreichelt'), null=True, blank=True)

    objects = CatQuerySet.as_manager()

    class Meta:
        verbose_name = _('Katze')
        verbose_name_plural = _('Katzen')

    def __str__(self):
        return f'{self.name} ({self.get_colour_display()})'
