from django.contrib import admin

from .models import Topic, TopicItem


class TopicItemAdmin(admin.ModelAdmin):
    list_filter = ('topic', 'enable')


admin.site.register(Topic)
admin.site.register(TopicItem, TopicItemAdmin)
