from django.utils import timezone
from django.contrib.sitemaps import Sitemap
from blog.models import Post, Page

posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
pages = Page.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

sitemapPosts = {
    'queryset': posts,
    'date_field': 'published_date',
}
sitemapPages = {
    'queryset': pages,
    'date_field': 'published_date'
}

class StaticSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return ['/', '/blog/']
    
    def location(self,item):
        return item