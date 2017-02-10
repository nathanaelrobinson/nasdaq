from django.conf.urls import url
from . import views

app_name='stockmarket'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<stock_id>[0-9]+)/$', views.stockpage, name='stockpage'),
	url(r'^vote/$', views.vote, name='vote'),
	url(r'^(?P<stock_id>[0-9]+)/buy/$', views.buy, name='buy'),
	url(r'^(?P<stock_id>[0-9]+)/sell/$', views.sell, name='sell'),
]