from django.db import models  # noqa: F401


class Page(models.Model):
    class Meta:
        ordering = ['id']

    title = models.CharField()

    def __str__(self):
        return self.title


class ContentInfo(models.Model):
    class Meta:
        abstract = True
        ordering = ['sequence', 'id']

    counter = models.IntegerField(default=0)
    title = models.CharField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    sequence = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title


class Video(ContentInfo):
    video_url = models.URLField()
    subtitles_url = models.URLField()


class Audio(ContentInfo):
    bitrate = models.IntegerField(default=0)


class Text(ContentInfo):
    text = models.TextField()
