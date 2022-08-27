from rest_framework.views import APIView
from rest_framework import permissions, response, status, generics
from youtube.config.settings.django import YOUTUBE_SEARCH_URL, YOUTUBE_API_KEY
from videos.api.serializers import VideoSerializer
from videos.models import Video
from rest_framework.pagination import PageNumberPagination


class ViewListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.order_by("-published_at")
    serializer_class = VideoSerializer
    pagination_class = ViewListPagination
    ordering_fields = ["published_at"]
    search_fields = ["title", "description"]


class SearchVideoView(APIView):
    serializer_class = VideoSerializer
    search_fields = ["title", "description"]

    def get_queryset(self):
       return Video.objects.all()