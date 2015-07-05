from django.shortcuts import render

from ..hotsite.models import HotSite
from ..topic.models import Topic


def index(request):
    topics = Topic.objects.available()
    return render(request, "simple.html", {
        'topics': topics
    })
