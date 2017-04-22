from django.conf.urls import url, include
from django.contrib import admin
from ebdjango import settings
from main import views as main_views
from account import views as account_views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from products import views as product_views
from django.conf import settings
from threads import views as forum_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),  
    url(r'^$', main_views.get_index, name='index'),
    url(r'^contact$', main_views.get_contact, name='contact'),
    url(r'^about$', main_views.get_about, name='about'),
    url(r'^register/$', account_views.register, name='register'),
    url(r'^account/$', account_views.get_index, name='index'),
    url(r'^profile/$', account_views.profile, name='profile'),
    url(r'^login/$', account_views.login, name='login'),
    url(r'^logout/$', account_views.logout, name='logout'),
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
    url(r'^products/$', product_views.all_products),
    url(r'^account/', include('account.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #url(r'^/', include('polls.urls')),
       # url(r'^polls2/', include('polls2.urls')),
    #url(r'^now$', include('blog.urls')),
    #url(r'^(?P<slug>[\w\-]+)/$', include('blog.views.post')),
    #urlpatterns += patterns('django.views.static',(r'^media/(?P<path>.*)','serve',{'document_root':settings.MEDIA_ROOT}), ),
    # Forum URLs
    url(r'^forum/$', forum_views.forum),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', forum_views.thread_vote, name='cast_vote'),
    url(r'^thanks$', main_views.get_thanks, name='thanks'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
       url(r'^__debug__/', include(debug_toolbar.urls)),
   ]