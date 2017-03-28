"""Url to view mappings."""
from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.DiagnosesList.as_view(), name='DiagnosisListView'),
    url(r'^(?P<pk>\d+)/$', views.DiagnosesDetail.as_view(), name='DiagnosisDetailView')
]
