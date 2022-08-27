from threading import Thread
from celery import shared_task
from datetime import datetime
import json
import requests
from youtube.config.settings.django import YOUTUBE_SEARCH_URL
import logging
from videos.models import Video

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def save_videos(videos):
    try:
        for video in videos:
            Video.objects.get_or_create(
                video_id=video["id"]["videoId"],
                title=video["snippet"]["title"],
                description=video["snippet"]["description"],
                thumbnail=video["snippet"]["thumbnails"],
                published_at=video["snippet"]["publishedAt"],
            )
        logger.info("Saved videos in the database")
    except Video.DoesNotExist:
        logger.info("Error in saving videos in the database")


@shared_task
def search_videos(api_key):
    try:
        logger.info("Fetching latest videos")
        all_videos = []
        params = {
            "part": "snippet",
            "q": "cricket",
            "key": api_key,
            "maxResults": 10,
            "order": "date",
            "fields": "items(id(videoId),snippet(publishedAt,thumbnails,title,description))",
            "pageToken": "",
            "publishedAfter": datetime.utcfromtimestamp(
                (datetime.now().timestamp() - 900)
            ).strftime("%Y-%m-%dT%H:%M:%S.0Z"),
        }
        videos = json.loads(
            requests.request("GET", YOUTUBE_SEARCH_URL, params=params).text
        )
        all_videos = all_videos + videos["items"]
        nextPageToken = videos.get("nextPageToken")
        while nextPageToken:
            params["pageToken"] = nextPageToken
            videos = json.loads(
                requests.request("GET", YOUTUBE_SEARCH_URL, params=params).text
            )
            nextPageToken = videos.get("nextPageToken")
            all_videos = all_videos + videos["items"]
        save_videos(all_videos)
        # Thread(target=save_videos, args=(all_videos,)).start()
    except Exception as e:
        logging.info("Youtube API call failed")
