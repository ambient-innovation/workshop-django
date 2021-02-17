from rest_framework import serializers

from apps.account.models import EmailUser


class EmailUserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailUser
        fields = ('id', 'first_name', 'last_name', 'full_name')
