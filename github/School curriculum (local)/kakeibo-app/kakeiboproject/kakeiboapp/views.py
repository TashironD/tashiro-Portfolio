from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView#  リスト形式（表）で表示するためのListView
from .models import Record
from django.urls import reverse_lazy



class RecordListView(ListView):
    template_name="list.html"#templatesの中の"list.html"を画面に表示する
    model=Record#modelsのDBを使う

class RecordDetailView(DetailView):
    template_name="detail.html"
    model=Record

class RecordCreateView(CreateView):
    template_name="create.html"
    model=Record
    fields=("title","memo","type","amount","date")
    
    success_url=reverse_lazy("list")
    #success_urlは登録完了後にどのページに行くかを指定する。
    #reverse_lazyは("list")にリバースする

class RecordUpdateView(UpdateView):
    template_name="update.html"
    model=Record
    fields=("title","memo","type","amount","date")
    
    success_url=reverse_lazy("list")


class RecordDeleteView(DeleteView):
    template_name="delete.html"
    model=Record
    
    success_url=reverse_lazy("list")


