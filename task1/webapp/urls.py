from django.urls import path
from webapp.views.base import index_view
from webapp.views.stats import stats_view

urlpatterns= [
    path("", index_view),
    path("cat_stats", stats_view)
]