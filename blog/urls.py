from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.post_list, name="post_list"),
    #url(r'^/$', views.post_list, name="post_list"),
    #url(r'^/stuff/$', views.post_list, name="post_list"),
    url(r'^post/$', views.new_post, name='new_post'),
    url(r'(?P<id>\d+)/$', views.post_detail),
    url(r'^blog/(?P<id>\d+)/edit$', views.edit_post, name="edit"),
    #url(r'^popular/$', views.blog_posts_by_views, name="popular"),
    #url(r'^popular/$', views.blog_posts_by_tags, name="tags"),
]
