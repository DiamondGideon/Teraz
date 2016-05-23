from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from shop.models import *
from rest_framework import routers, serializers, viewsets
from mysite.routers import *


# Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^api/', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^auth/', include('loginsys.urls')),
    # url(r'^', include('shop.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]