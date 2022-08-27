from django.db import models
from django.utils.translation import gettext_lazy as _
from youtube.common.models import TimeStampedModel


class Video(TimeStampedModel):

    video_id = models.CharField(_("Video ID"), max_length=255, unique=True)
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    thumbnail = models.JSONField(
        _("Thumbnail"),
        blank=True,
        default=dict,
        help_text=_("Thumbnails of different resolutions."),
    )
    published_at = models.DateTimeField(_("Published at"), blank=True, null=True)

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return self.title

class APIKey(TimeStampedModel):

    key = models.CharField(_("Key"), max_length=255, unique=True)
    priority = models.IntegerField(_("Priority"), default=0)

    class Meta:
        verbose_name = _("API Key")
        verbose_name_plural = _("API Keys")

    def __str__(self):
        return self.key 