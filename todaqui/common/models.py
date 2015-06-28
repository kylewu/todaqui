from django.db import models


class OrderedModel(models.Model):
    order = models.SmallIntegerField(default=1)
    enable = models.BooleanField(db_index=True, default=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'({})'.format(self.order)
