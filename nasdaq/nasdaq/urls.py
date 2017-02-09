from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^stockmarket/', include('stockmarket.urls', namespace='stockmarket')),
]
