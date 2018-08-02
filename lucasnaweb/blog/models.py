from django.db import models
from django.utils import timezone
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, blank=True)
    subtitle = models.CharField(max_length=200, default='')
    text = models.TextField()
    jumbotron = models.ImageField(null=False, default='header-blog-posts.jpg')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    keywords = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def save(self,*args, **kwargs):
        if not self.published_date:
            self.published_date = timezone.now()
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post,self).save()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/blog/post/'+self.slug+'/'

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, blank=True)
    subtitle = models.CharField(max_length=200, default='')
    text = models.TextField()
    jumbotron = models.ImageField(null=False, default='header-blog-posts.jpg')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    keywords = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def save(self,*args, **kwargs):
        if not self.published_date:
            self.published_date = timezone.now()
        if not self.slug:
            self.slug = slugify(self.title)
        super(Page,self).save()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return '/'+self.slug+'/'