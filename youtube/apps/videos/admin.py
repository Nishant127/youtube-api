from re import A
from django.contrib import admin
from videos.models import Video, APIKey

admin.site.register(Video)
admin.site.register(APIKey)
