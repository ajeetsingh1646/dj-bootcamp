from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import FileSystemStorage

# saving protected media to a new location from default location
PROTECTED_MEDIA = getattr(settings, 'PROTECTED_MEDIA', None)

if PROTECTED_MEDIA == None:
    raise ImproperlyConfigured("PROTECTED_MEDIA is not set in settings.py")


class ProtectedStorage(FileSystemStorage):
    location = PROTECTED_MEDIA  # MEDIA_ROOT
