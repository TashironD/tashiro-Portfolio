
from django.urls import path
from . import views


urlpatterns = [
    path("top/",views.TopView.as_view(),name="top"),
    path("ranking/",views.RankingView.as_view(),name="ranking"),
]
