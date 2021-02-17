from django.contrib import admin

from apps.cat.models import Cat, Hideout, Food
from apps.core.admin import CommonInfoAdminMixin


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(Hideout)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(Cat)
class CatAdmin(CommonInfoAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'owner', 'colour')
    list_filter = ('owner',)
