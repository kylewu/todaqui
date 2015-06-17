from django.db import models


class HotSite(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField(max_length=512)
    img_name = models.CharField(max_length=16)
