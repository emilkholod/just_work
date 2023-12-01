import logging
import os

from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate

logger = logging.getLogger(__name__)


def generate_superuser(**kwargs):
    """
    Generate superuser
    """
    username = os.getenv('DJANGO_SUPERUSER_USERNAME')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL')

    user = get_user_model()

    if user.objects.filter(username=username, email=email).exists():
        logger.debug('Superuser already created!')
    else:
        logger.info('Creating new superuser')
        admin = user.objects.create_superuser(username=username, password=password, email=email)
        admin.save()


class VideoLibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysite.blog'

    def ready(self):
        """
        Run on registry ready
        """
        post_migrate.connect(generate_superuser, sender=self)
