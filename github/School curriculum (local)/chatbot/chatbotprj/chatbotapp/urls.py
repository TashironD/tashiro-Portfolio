
from django.urls import path,include
from . import views

app_name="chatbotapp"

urlpatterns = [
    path("",views.Index.as_view(),name="Index"),
    path("chatbot/",views.BotApiView.as_view(),name="chatbot"),
]