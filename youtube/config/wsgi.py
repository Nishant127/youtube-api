"""
WSGI config for youtube project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from threading import Thread
from youtube.apps.videos.service import YoutubeVideoService

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youtube.config.settings.django")

application = get_wsgi_application()

Thread(target=YoutubeVideoService.save_youtube_videos, args=()).start()
