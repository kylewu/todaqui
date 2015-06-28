from django.db import models

from ..common.models import OrderedModel


class HotSite(OrderedModel):
    name = models.CharField(max_length=64)
    link = models.URLField(max_length=512)
    img_name = models.CharField(max_length=16)

    def __unicode__(self):
        return '{} {}'.format(super(HotSite, self).__unicode__(), self.name)

    def get_absolute_url(self):
        return self.link
