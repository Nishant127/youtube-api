from rest_framework.views import APIView
from rest_framework import permissions, response, status, generics
from youtube.config.settings.django import YOUTUBE_SEARCH_URL
from videos.api.serializers import VideoSerializer
from videos.models import Video, APIKey
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


class SearchVideoView(generics.ListAPIView):
    serializer_class = VideoSerializer
    search_fields = ["title", "description"]

    def get_queryset(self):
        return Video.objects.all()


class APIKeyView(APIView):
    def post(self, request):
        api_key = request.data.get("api_key")
        try:
            if not APIKey.objects.exists():
                APIKey.objects.create(key=api_key, in_use=True)
            else:
                APIKey.objects.create(key=api_key)
            return response.Response(
                data="API key added successfully", status=status.HTTP_200_OK
            )
        except:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
