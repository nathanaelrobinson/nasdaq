from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^', include('stockmarket.urls', namespace='stockmarket')),
	url(r'^snippets/', include('snippets.urls', namespace='snippets')),
    url(r'^admin/', include(admin.site.urls)),
]

