from django.urls import path

from trails.apps import TrailsConfig
from trails.views import ClusterInfoNalichevoView, ParkListView, InformationNalychevoViews

app_name = TrailsConfig.name

urlpatterns = [
    path('cluster_info_nalichevo', ClusterInfoNalichevoView.as_view(), name='cluster_info_nalichevo'),
    path('parks', ParkListView.as_view(), name='parks'),
    path('information_nalychevo', InformationNalychevoViews.as_view(), name='information_nalychevo'),
]
