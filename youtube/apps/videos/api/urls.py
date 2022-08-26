from django.urls import path
from videos.api import views

urlpatterns = [path("search/", views.VideoView.as_view(), name="search_video")]
