from django.shortcuts import render

from ..hotsite.models import HotSite
from ..topic.models import Topic


def index(request):
    hotsites = HotSite.objects.all()
    topics = Topic.objects.filter(enable=True)
    return render(request, "index.html", {
        'hotsites': hotsites,
        'topics': topics
    })
