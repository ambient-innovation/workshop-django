class CommonInfoAdminMixin:

    def get_readonly_fields(self, request, obj=None):
        return super().get_readonly_fields(request, obj) + ('created_by', 'lastmodified_by', 'created_at',
                                                            'lastmodified_at')

    def save_form(self, request, form, change):
        if form.instance and request.user:
            if not form.instance.id:
                form.instance.created_by = request.user
            form.instance.lastmodified_by = request.user

        return super().save_form(request, form, change)
