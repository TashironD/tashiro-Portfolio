from typing import ItemsView
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Item
from .serializers import ItemSerializer

from rest_framework.generics import RetrieveAPIView

class StockListView(ListView):
    model=Item
    template_name="list.html"


class StockAPIView(RetrieveAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer