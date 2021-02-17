from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.account.managers import EmailUserManager


class EmailUser(PermissionsMixin, AbstractBaseUser):
    """
    Standard email user
    E-Mail is login name instead of username
    """
    LENGTH_FIRST_NAME = LENGTH_LAST_NAME = 100
    USERNAME_FIELD = EMAIL_FIELD = 'email'

    email = models.EmailField(_('E-Mail-Adresse'), max_length=255, unique=True)

    first_name = models.CharField(_('Vorname'), max_length=LENGTH_FIRST_NAME, blank=True, null=True)
    last_name = models.CharField(_('Nachname'), max_length=LENGTH_LAST_NAME, blank=True, null=True)
    is_active = models.BooleanField(_('Aktiv'), default=False)

    objects = EmailUserManager()

    class Meta:
        db_table = 'auth_user'
        ordering = ['email']
        verbose_name = _('Benutzer')
        verbose_name_plural = _('Benutzer')

    def __str__(self):
        return self.full_name

    @property
    def group_name(self):
        if self.is_superuser:
            return _('Administrator (Superuser)')

        if self.groups.count() > 1:
            return ', '.join(
                [obj.split(" ", 1)[1] for obj in self.groups.values_list('name', flat=True)]
            )
        else:
            return ''.join(
                [obj.split(" ", 1)[1] for obj in self.groups.values_list('name', flat=True)]
            )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        """
        Only superuser can login to Django-Admin
        """
        return self.is_superuser
