from django.db import models


class BaseTopic(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    order = models.SmallIntegerField(default=1, unique=True)
    enable = models.BooleanField(db_index=True, default=True)

    class Meta:
        abstract = True


class BaseItem(models.Model):
    name = models.CharField(max_length=32)
    link = models.URLField(max_length=512)
    order = models.SmallIntegerField(default=1)

    class Meta:
        abstract = True


class Topic(BaseTopic):

    def __unicode__(self):
        return u'{}: {} (/{})'.format(self.order, self.name, self.slug)

    def get_absolute_url(self):
        return u'/{}'.format(self.slug)


class TopicItem(BaseItem):
    topic = models.ForeignKey(Topic)

    class Meta:
        unique_together = (("topic", "order"),)

    def __unicode__(self):
        return u'({}:{}) {}'.format(self.topic.name, self.order, self.name)

    def get_absolute_url(self):
        return self.link


class SubTopic(BaseTopic):
    topic = models.ForeignKey(Topic)

    def __unicode__(self):
        return u'{}: {} -> {} (/{})'.format(
            self.order, self.topic.name, self.name, self.slug)

    def get_absolute_url(self):
        return u'/{}'.format(self.slug)


class SubTopicItem(BaseItem):
    subtopic = models.ForeignKey(SubTopic)

    class Meta:
        unique_together = (("subtopic", "order"),)

    def __unicode__(self):
        return u'({}) {}'.format(self.subtopic.name, self.name)

    def get_absolute_url(self):
        return self.link
