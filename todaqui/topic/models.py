from django.db import models
from ..common.models import OrderedModel


class BaseTopic(OrderedModel):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'{}: {}'.format(
            super(BaseTopic, self).__unicode__(), self.name)


class BaseItem(OrderedModel):
    name = models.CharField(max_length=32)
    link = models.URLField(max_length=512)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'{}: {}'.format(super(BaseItem, self).__unicode__(), self.name)


class Topic(BaseTopic):

    def get_absolute_url(self):
        return u'/{}'.format(self.slug)

    def frontpage_items(self):
        return SubTopicItem.objects.filter(
            shown_in_frontpage=True,
            subtopic__topic=self)


class SubTopic(BaseTopic):
    topic = models.ForeignKey(Topic)

    def __unicode__(self):
        return u'({}) -> {}'.format(
            self.topic.name, super(SubTopic, self).__unicode__())

    def get_absolute_url(self):
        return u'/{}'.format(self.slug)


class SubTopicItem(BaseItem):
    subtopic = models.ForeignKey(SubTopic)

    shown_in_frontpage = models.BooleanField(default=False)
    frontpage_order = models.SmallIntegerField(default=1)

    class Meta:
        unique_together = (("subtopic", "order"),)

    def __unicode__(self):
        return u'{} ({})'.format(
            super(SubTopicItem, self).__unicode__(),
            self.subtopic.name)

    def get_absolute_url(self):
        return self.link
