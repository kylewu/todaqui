from django.shortcuts import render

from ..hotsite.models import HotSite
from ..topic.models import Topic


def index(request):
    hotsites = HotSite.objects.available()
    topics = Topic.objects.available()
    return render(request, "index.html", {
        'hotsites': hotsites,
        'topics': topics
    })
