from django.conf.urls import url
from . import views

app_name='stockmarket'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<stock_id>[0-9]+)/$', views.stockpage, name='stockpage'),
	url(r'^vote/$', views.vote, name='vote'),
	url(r'^buyandsell/(?P<stock_id>[0-9]+)/$', views.buyandsell, name='buyandsell'),
]