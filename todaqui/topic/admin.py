from django.contrib import admin

from .models import Topic, SubTopic, SubTopicItem


class SubTopicItemInline(admin.TabularInline):
    model = SubTopicItem


class SubTopicAdmin(admin.ModelAdmin):
    list_filter = ('topic', )
    inlines = [SubTopicItemInline, ]


admin.site.register(Topic)
admin.site.register(SubTopic, SubTopicAdmin)
