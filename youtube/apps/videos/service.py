from youtube.config.settings.django import YOUTUBE_SEARCH_URL, YOUTUBE_API_KEY
import json
import requests
from videos.models import Video
from rest_framework import permissions, response, status
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def search_videos(search_query):
    try:
        params = {
            "part": "snippet",
            "q": search_query,
            "key": YOUTUBE_API_KEY,
            "maxResults": 5,
            "order": "date",
            "fields": "items(id(videoId),snippet(publishedAt,thumbnails,title,description))",
        }
        videos = json.loads(
            requests.request("GET", YOUTUBE_SEARCH_URL, params=params).text
        )

        for video in videos["items"]:
            Video.objects.get_or_create(
                video_id=video["id"]["videoId"],
                title=video["snippet"]["title"],
                description=video["snippet"]["description"],
                thumbnail=video["snippet"]["thumbnails"],
                published_at=video["snippet"]["publishedAt"],
            )
    except Exception as e:
        logging.info("API call failed")
