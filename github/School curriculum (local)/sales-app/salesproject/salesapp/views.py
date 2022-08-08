from django.shortcuts import render

from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView

# Create your views here.

from .models import Sales
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse,reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class SalesListView(ListView):
    template_name="list.html"
    model=Sales
    

@login_required
def listview(request):
    lists=Sales.objects.all()
    return render(request,"list.html",{"object_list":lists})
    #render:画面を作る。



class SalesDetailView(LoginRequiredMixin,DetailView):
    template_name="detail.html"
    model=Sales


class SalesUpdateView(LoginRequiredMixin,UpdateView):
    template_name="update.html"
    model=Sales
    fields=("customer","progress","manager_checked","memo","staff")
    success_url=reverse_lazy("list")



class SalesCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name="create.html"
    model=Sales
    fields=("customer","progress","manager_checked","memo","staff")
    success_url=reverse_lazy("list")
    success_message="営業データが追加されました。"


class SalesDeleteView(LoginRequiredMixin,DeleteView):
    template_name="delete.html"
    model=Sales
    success_url=reverse_lazy("list")



def manager_check(request,pk):#----------------------------------------------------------------------
    if request.user.is_superuser and request.method == "POST":
        try:
            sales=Sales.objects.get(pk=pk)
        except Sales.DoesNotExist:
            pass
        else:
            sales.manager_checked =not sales.manager_checked
            sales.save()

            messages.success(request,"チェック状況が更新されました.")

            return redirect(reverse("list"))

    return redirect(reverse("list"))





   