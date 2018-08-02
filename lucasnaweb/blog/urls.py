from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:post_id>/', views.post_detail, name='post_detail'),
]