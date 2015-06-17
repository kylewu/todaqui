from django.contrib.sitemaps import Sitemap

from .topic.models import Topic


class TopicSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return Topic.objects.all()

    def lastmod(self, obj):
        import datetime
        return datetime.datetime.now()


sitemaps = {
    'topic': TopicSitemap,
}
