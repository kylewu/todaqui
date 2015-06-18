from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    order = models.SmallIntegerField(default=1, unique=True)

    def __unicode__(self):
        return u'{}: {} (/{})'.format(self.order, self.name, self.slug)

    def get_absolute_url(self):
        return u'/{}'.format(self.slug)


class TopicItem(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=32)
    link = models.URLField(max_length=512)
    order = models.SmallIntegerField(default=1)

    class Meta:
        unique_together = (("topic", "order"),)

    def __unicode__(self):
        return u'({}) {}'.format(self.topic.name, self.name)

    def get_absolute_url(self):
        return self.link


class SubTopic(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    order = models.SmallIntegerField(default=1, unique=True)

    def __unicode__(self):
        return u'{}: {} -> {} (/{})'.format(
            self.order, self.topic.name, self.name, self.slug)

    def get_absolute_url(self):
        return u'/{}'.format(self.slug)


class SubTopicItem(models.Model):
    subtopic = models.ForeignKey(SubTopic)
    name = models.CharField(max_length=32)
    link = models.URLField(max_length=512)
    order = models.SmallIntegerField(default=1)

    class Meta:
        unique_together = (("subtopic", "order"),)

    def __unicode__(self):
        return u'({}) {}'.format(self.subtopic.name, self.name)

    def get_absolute_url(self):
        return self.link
