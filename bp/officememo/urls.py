from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^add/$', add, name='index'),
    url(r'^card/+(?P<proj_id>\d+)$',card, name='card'),
    #url(r'^delete/+(?P<id>\d+)$',delete, name='delete'),
    url(r'^approve/+(?P<proj_id>\d+)$',approve, name='approve'),
    url(r'^approve/+(?P<proj_id>\d+)$',approve, name='approve'),
)
