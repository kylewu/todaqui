from django.db import models


class OrderedManager(models.Manager):

    def get_queryset(self):
        return super(OrderedManager, self).get_queryset().order_by('order')

    def ordered(self):
        return self.get_queryset().order_by('order')

    def available(self):
        return self.get_queryset().filter(enable=True)


class OrderedModel(models.Model):
    order = models.SmallIntegerField(default=1)
    enable = models.BooleanField(db_index=True, default=True)

    objects = OrderedManager()

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'({})'.format(self.order)
