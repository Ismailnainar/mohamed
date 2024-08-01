# image_api/serializers.py

from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    image_path_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('id', 'name', 'image_path', 'image_path_url', 'created_at')

    def get_image_path_url(self, obj):
        # Assuming obj.image_path is not None, you can get its URL
        if obj.image_path:
            return obj.image_path.url
        else:
            return None
