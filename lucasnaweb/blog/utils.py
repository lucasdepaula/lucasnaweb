from django.utils import timezone
from django.contrib.sitemaps import Sitemap
from blog.models import Post

sitemapDict = {
    'queryset': Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date'),
    'date_field': 'published_date',
}

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    def lastmod(self, obj):
        return obj.pub_date