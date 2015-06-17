from django.shortcuts import render

from ..hotsite.models import HotSite


def index(request):
    hotsites = HotSite.objects.all()
    return render(request, "index.html", {
        'hotsites': hotsites
    })
