import logging
import os

from django.contrib.auth import get_user_model
from django.db import migrations

logger = logging.getLogger(__name__)


def create_superuser(apps, schema_editor):
    """
    Create superuser
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


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
