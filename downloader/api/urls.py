from django.urls import path

from api.views import DownloadView, ListTypeChoices

app_name = "api_urls"

v1_urlpatterns = [
    path("download/", DownloadView.as_view(), name="download"),
    path("type-choices/", ListTypeChoices.as_view(), name="list_type_choices"),
]

urlpatterns = []

urlpatterns += v1_urlpatterns
