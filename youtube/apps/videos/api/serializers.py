from videos.models import Video
from rest_framework import serializers

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "_all_"