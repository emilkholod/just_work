import logging

from django.db import migrations

logger = logging.getLogger(__name__)


def load_data(apps, schema_editor):
    """
    Load data to database
    """
    app = 'blog'
    Page = apps.get_model(app, 'Page')
    Page.objects.create(title='Page By Ivanov')
    page2 = Page.objects.create(title='Page By Petrov')
    Page.objects.create(title='Page By Sidorov')

    Audio = apps.get_model(app, 'Audio')
    Audio.objects.create(title='Jingle Bells', bitrate=128, page=page2)
    Audio.objects.create(title='Jingle Bells (remix)', bitrate=128, page=page2)

    Text = apps.get_model(app, 'Text')
    Text.objects.create(title='Jingle Bells Text', text='some long long text')

    Video = apps.get_model(app, 'Video')
    Video.objects.create(
        title='Home Alone',
        video_url='home-alone.com/video',
        subtitles_url='home-alone.com/subtitles',
        page=page2,
        sequence=10,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_create_superuser'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]
