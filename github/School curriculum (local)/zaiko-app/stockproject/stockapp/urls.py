
from django.urls import path
from .views import StockListView,StockAPIView

urlpatterns = [
    path("list/",StockListView.as_view(),name="list"),
    path("api/<int:pk>/",StockAPIView.as_view()),

]
