from django.conf.urls import url
from . import views as account_views

urlpatterns=[
    #url(r'^admin/', admin.site.urls),
    url(r'^register/$', account_views.register, name='register'),
    url(r'^profile/$', account_views.profile, name='profile'),
    url(r'^login/$', account_views.login, name='login'),
    url(r'^logout/$', account_views.logout, name='logout'),


]