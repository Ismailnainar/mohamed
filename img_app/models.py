# models.py

from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=100)
    image_path = models.FileField(upload_to='images/')  # Assuming you want to store the image file
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Image'
