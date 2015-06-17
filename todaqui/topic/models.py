from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    order = models.SmallIntegerField(default=1, unique=True)

    def __unicode__(self):
        return u'%s (/%s)' % (self.name, self.slug)

    def get_absolute_url(self):
        return u'/' + self.slug


class TopicItem(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=32)
    link = models.URLField(max_length=512)
    order = models.SmallIntegerField(default=1, unique=True)

    def __unicode__(self):
        return u'(%s) %s' % (self.topic.name, self.name)

    def get_absolute_url(self):
        return self.link
