from django.conf.urls import *
from django.conf import settings
from home import views as home_views
from .models import Events
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, DetailView

urlpatterns = [
	url(r'^login$', auth_views.login),
    url(r'^logout$', auth_views.logout),
	url(r'^register$',home_views.register,name='register'),

    url(r'^$',home_views.event_ft,name='event_ft'),
    url(r'^event_bk$',home_views.event_bk,name='event_bk'),
	url(r'^event_bk_update/(?P<id>[\d]+)$',home_views.event_bk_update,name='event_bk_update'),
	url(r'^event_bk_remove/(?P<id>[\d]+)$',home_views.event_bk_remove,name='event_bk_remove'),
	url(r'^(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(model=Events,),name='events_detail'),
	
	url(r'^location_bk$',home_views.location_bk,name='location_bk'),
	url(r'^location_bk_update/(?P<id>[\d]+)$',home_views.location_bk_update,name='location_bk_update'),
	url(r'^location_bk_remove/(?P<id>[\d]+)$',home_views.location_bk_remove,name='location_bk_remove'),
	
	url(r'^category_bk$',home_views.category_bk,name='category_bk'),
	url(r'^category_bk_update/(?P<id>[\d]+)$',home_views.category_bk_update,name='category_bk_update'),
	url(r'^category_bk_remove/(?P<id>[\d]+)$',home_views.category_bk_remove,name='category_bk_remove'),
]