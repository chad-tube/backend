from django.urls import path

from api.views import DownloadView

app_name = "api_urls"

v1_urlpatterns = [
    path("download/", DownloadView.as_view(), name="download"),
]

urlpatterns = []

urlpatterns += v1_urlpatterns
