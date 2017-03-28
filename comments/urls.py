"""Url to views mappings."""
from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.CommentsList.as_view(), name='CommentsListView'),
    url(r'^(?P<pk>\d+)/$', views.CommentsDetail.as_view(), name='CommentsDetail')
]
