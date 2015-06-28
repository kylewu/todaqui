from django.core.management.base import BaseCommand

import feedparser
from dateutil.parser import parse

from todaqui.rssnews.models import News

YAHOO_RSS = 'http://estaticos.elmundo.es/elmundo/rss/espana.xml'


class Command(BaseCommand):
    help = 'fetch latest news from rss feed'

    def add_arguments(self, parser):
        parser.add_argument('--num', default=5, type=int)
        parser.add_argument('--feed', required=False, default=YAHOO_RSS)

    def handle(self, *args, **options):
        feed = feedparser.parse(options['feed'])

        n = 0
        for e in feed['entries']:
            if 'media_thumbnail' not in e:
                continue
            i_space = e['summary'].find('&nbsp;')
            if not i_space:
                continue

            n += 1

            try:
                created = parse(e['published'])
                News.objects.create(
                    link=e['links'][0]['href'],
                    summary=e['summary'][:i_space],
                    created=created)
            except Exception as e:
                print e
                continue

            if n == options['num']:
                break
