from ai_django_core.managers import AbstractUserSpecificQuerySet


class CatQuerySet(AbstractUserSpecificQuerySet):

    def visible_for(self, user):
        return self.filter(owner=user)

    def editable_for(self, user):
        return self.visible_for(user)

    def deletable_for(self, user):
        return self.visible_for(user)
