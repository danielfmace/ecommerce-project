from django.conf.urls import patterns, url

from rides import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'index'}),
    )