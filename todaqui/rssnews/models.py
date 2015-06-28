from django.db import models


class News(models.Model):
    link = models.URLField()
    summary = models.CharField(max_length=512)
    created = models.DateTimeField()

    def __unicode__(self):
        return self.summary
