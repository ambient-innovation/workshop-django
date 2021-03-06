from django.conf import settings
from django.core.files.storage import FileSystemStorage
from storages.backends.s3boto3 import S3Boto3Storage


class PrivateMediaStorage(S3Boto3Storage):
    location = settings.AWS_PRIVATE_MEDIA_LOCATION
    querystring_expire = 3600  # seconds until the generated link expires
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False


if settings.AWS_PRIVATE_MEDIA_LOCATION:
    PRIVATE_FILE_STORAGE = PrivateMediaStorage()
else:
    file_system_storage = FileSystemStorage(location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL)
    PRIVATE_FILE_STORAGE = file_system_storage


class PublicMediaStorage(S3Boto3Storage):
    location = settings.AWS_PUBLIC_MEDIA_LOCATION

    def path(self, name):
        pass
