from django.urls import path
from videos.api import views

urlpatterns = [
    path("search/", views.SearchVideoView.as_view(), name="search_video"),
    path("", views.VideoListView.as_view(), name="video_list"),
]
