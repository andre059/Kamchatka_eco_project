from django.urls import path

from trails.apps import TrailsConfig
from trails.views import ClusterInfoNalichevoView

app_name = TrailsConfig.name

urlpatterns = [
    path('cluster_info_nalichevo', ClusterInfoNalichevoView.as_view(), name='cluster_info_nalichevo'),
]
