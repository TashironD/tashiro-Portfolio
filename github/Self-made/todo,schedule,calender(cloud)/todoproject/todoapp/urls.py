from django.urls import path

from . import views

urlpatterns = [

    path("",views.index,name="index"),

    path("list/",views.ListView.as_view(),name="list"),
    path("calender/",views.Calender,name="calender"),
    path("create/",views.CreateView.as_view(),name="create"),
    path("update<int:pk>/",views.UpdateView.as_view(),name="update"),
    path("delete<int:pk>/",views.DeleteView.as_view(),name="delete"),
    path("done-check<int:pk>/",views.done_check,name="done-check"),

    path("calender/get_event/",views.get_events,name="get_event"),
]
