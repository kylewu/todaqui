from django.db import models
from ..common.models import OrderedModel


class BaseTopic(OrderedModel):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'{}: {} (/{})'.format(
            super(BaseTopic, self).__unicode__(), self.name, self.slug)


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


class TopicItem(BaseItem):
    topic = models.ForeignKey(Topic)

    class Meta:
        unique_together = (("topic", "order"),)

    def __unicode__(self):
        return u'{} ({})'.format(
            super(TopicItem, self).__unicode__(),
            self.topic.name)

    def get_absolute_url(self):
        return self.link


class SubTopic(BaseTopic):
    topic = models.ForeignKey(Topic)

    def __unicode__(self):
        return u'(topic {}) {}'.format(
            self.topic.name, super(SubTopic, self).__unicode__())

    def get_absolute_url(self):
        return u'/{}'.format(self.slug)


class SubTopicItem(BaseItem):
    subtopic = models.ForeignKey(SubTopic)

    class Meta:
        unique_together = (("subtopic", "order"),)

    def __unicode__(self):
        return u'{} ({})'.format(
            super(SubTopicItem, self).__unicode__(),
            self.subtopic.name)

    def get_absolute_url(self):
        return self.link
