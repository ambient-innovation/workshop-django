from ai_django_core.managers import AbstractUserSpecificQuerySet
from django.contrib.auth.models import BaseUserManager


class EmailUserQuerySet(AbstractUserSpecificQuerySet):
    def visible_for(self, user):
        return self.all()

    def editable_for(self, user):
        return self.visible_for(user)

    def deletable_for(self, user):
        return self.visible_for(user)

    def no_superuser(self):
        """
        Returns a list of non-superusers
        """
        return super().filter(is_superuser=False)

    def get_active(self):
        """
        Returns a list of active users
        """
        return self.filter(is_active=True)


class EmailUserManager(BaseUserManager):
    def get_queryset(self):
        return EmailUserQuerySet(self.model, using=self._db)

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Email address is required.')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """

        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
