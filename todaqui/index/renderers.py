from django_medusa.renderers import StaticSiteRenderer


class IndexRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            "/",
        ])

renderers = [IndexRenderer, ]
