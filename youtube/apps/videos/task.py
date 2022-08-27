from threading import Thread
from celery import shared_task
from datetime import datetime
import json
import requests
from youtube.config.settings.django import YOUTUBE_SEARCH_URL, YOUTUBE_API_KEY
import logging
from videos.models import Video

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def save_videos(videos):
    logger.info("Saving videos in the database")
    for video in videos:
        Video.objects.get_or_create(
            video_id=video["id"]["videoId"],
            title=video["snippet"]["title"],
            description=video["snippet"]["description"],
            thumbnail=video["snippet"]["thumbnails"],
            published_at=video["snippet"]["publishedAt"],
        )


@shared_task
def search_videos(api_key):
    try:
        logger.info("Fetching latest videos")
        params = {
            "part": "snippet",
            "q": "cricket",
            "key": api_key,
            "maxResults": 10,
            "order": "date",
            "fields": "items(id(videoId),snippet(publishedAt,thumbnails,title,description))",
            "publishedAfter": datetime.utcfromtimestamp(
                (datetime.now().timestamp() - 900)
            ).strftime("%Y-%m-%dT%H:%M:%S.0Z"),
        }
        videos = json.loads(
            requests.request("GET", YOUTUBE_SEARCH_URL, params=params).text
        )
        Thread(target=save_videos, args=(videos["items"],)).start()
    except Exception as e:
        logging.info("API call failed")
