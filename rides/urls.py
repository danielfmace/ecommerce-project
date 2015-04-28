from django.conf.urls import patterns, url

from rides import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^search/$', views.search, name='search'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'index'}),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^schedule/$', views.schedule, name='schedule'),
    url(r'^cancel/$', views.cancel, name='cancel'),
    url(r'^account/$', views.account, name='account'),
    url(r'^pastDrive/(?P<ride_id>\d+)/$', views.pastDrive, name='pastDrive'),
    url(r'^pastRide/(?P<ride_id>\d+)/$', views.pastRide, name='pastRide'),
    url(r'^account/reviews/$', views.reviews, name='reviews'),
    url(r'^cancelDrive/$', views.cancelDrive, name='cancelDrive'),
    )
