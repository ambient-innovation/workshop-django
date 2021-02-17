from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _

from apps.account.models import EmailUser


@admin.register(EmailUser)
class EmailUserAdmin(UserAdmin):
    # form = EmailUserChangeForm
    # add_form = EmailUserCreateForm
    list_filter = ('is_superuser', 'is_active', 'groups')
    list_display = ('__str__', 'email', 'is_active', 'is_superuser')
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ('last_login',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': (
            'password',
        )}),
        (_('Persönliche Daten'), {'fields': (
            'first_name',
            'last_name',
        )}),
        (_('Kontakt'), {'fields': (
            'email',
        )}),
        (_('Berechtigungen'), {'fields': (
            'is_active',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
        (_('Informationen'), {'fields': (
            'last_login',
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
            )}),
    )

    def get_queryset(self, request):
        return super().get_queryset(request)


admin.site.register(Permission)
