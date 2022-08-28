from youtube.config.settings.django import YOUTUBE_SEARCH_URL
import json
import requests
from videos.models import Video, APIKey
from rest_framework import permissions, response, status
import logging
from datetime import datetime
from threading import Thread
from videos.task import search_videos
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class YoutubeVideoService:
    # Method to get YouTube API key
    @classmethod
    def get_api_key(cls):
        try:
            api_key = APIKey.objects.get(in_use=True, is_exhausted=False)
            if cls.is_api_key_exhausted(api_key.key):
                api_key.is_exhausted = True
                api_key.in_use = False
                api_key.save()
                logger.info("API key is exhausted, getting new API key")
                return cls.get_new_api_key()
            else:
                return api_key.key
        except APIKey.DoesNotExist:
            logger.info("No API key available, all API keys are exhausted")

    # Method to get new YouTube API key, if the current API key is exhausted
    @classmethod
    def get_new_api_key(cls):
        new_api_key = APIKey.objects.filter(is_exhausted=False).first()
        if new_api_key:
            new_api_key.in_use = True
            new_api_key.save()
            return new_api_key.key
        else:
            logger.info("No API key available")

    # Method to check if API key is exhausted
    @classmethod
    def is_api_key_exhausted(cls, api_key):
        params = {
            "part": "snippet",
            "q": "cricket",
            "key": api_key,
            "maxResults": 10,
            "order": "date",
            "fields": "items(id(videoId),snippet(publishedAt,thumbnails,title,description))",
            "publishedAfter": datetime.utcfromtimestamp(
                (datetime.now().timestamp())
            ).strftime("%Y-%m-%dT%H:%M:%S.0Z"),
        }
        videos = json.loads(
            requests.request("GET", YOUTUBE_SEARCH_URL, params=params).text
        )
        if videos.get("error"):
            return True
        return False

    # Method to fetch latest videos from YouTube and save in the database at an interval of 1 minute
    @classmethod
    def save_youtube_videos(cls):
        while True:
            time.sleep(60)
            api_key = cls.get_api_key()
            Thread(target=search_videos, args=(api_key,)).start()

    # Method to renew exhausted YouTube API key
    @classmethod
    def renew_api_key(cls):
        while True:
            time.sleep(86400)
            api_keys = APIKey.objects.filter(is_exhausted=True)
            for api_key in api_keys:
                time_elapsed = (
                    datetime.now().timestamp() - api_key.updated_at.timestamp()
                )
                if time_elapsed >= 86400:
                    api_key.is_exhausted = False
                    api_key.save()
                    logger.info("API key renewed")
