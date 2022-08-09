from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,UpdateView,CreateView,DeleteView

from .models import todolist

from django.shortcuts import redirect
from django.urls import reverse,reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.template import loader
from django.http import HttpResponse


#エラーの詳細を出すため
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError
@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)



def index(request):
    return render(request,"index.html")


class ListView(ListView):
    template_name="list.html"
    model=todolist


from django.middleware.csrf import get_token

def Calender(request):
    # CSRFのトークンを発行する
    get_token(request)
    template = loader.get_template("calender.html")
    return HttpResponse(template.render())
    


class CreateView(CreateView):
    template_name="create.html"
    model=todolist
    fields=("title","memo","type","start_date","end_date")
    success_url=reverse_lazy("list")


class UpdateView(UpdateView):
    template_name="update.html"
    model=todolist
    fields=("title","memo","type","start_date","end_date","done")
    success_url=reverse_lazy("list")


class DeleteView(DeleteView):
    template_name="delete.html"
    model=todolist
    success_url=reverse_lazy("list")


def done_check(request,pk):#----------------------------------------------------------------------
    #if request.user.is_superuser and request.method == "POST":
        try:
            DONE=todolist.objects.get(pk=pk)#Salesデータベースにpkに紐づくデータを取りに行く
        except todolist.DoesNotExist:#データが見つからない場合に実行される
            pass
        else:
            DONE.done =not DONE.done #notで反転させる。
            DONE.save()

            messages.success(request,"チェック状況が更新されました.")

            return redirect(reverse("list"))

    #return redirect(reverse("list"))





from django.http import JsonResponse
from .forms import CalendarForm
import json
from .models import todolist
from .forms import CalendarForm
from django.http import Http404
import time
from django.middleware.csrf import get_token
from django.template import loader
from django.http import HttpResponse


def get_events(request):
    """
    イベントの取得
    """

    if request.method == "GET":
        # GETは対応しない
        raise Http404()

    # JSONの解析
    datas = json.loads(request.body)

    # バリデーション
    calendarForm = CalendarForm(datas)
    if calendarForm.is_valid() == False:
        # バリデーションエラー
        raise Http404()

    # リクエストの取得
    start_date = datas["start_date"]
    end_date = datas["end_date"]

    # 日付に変換。JavaScriptのタイムスタンプはミリ秒なので秒に変換
    formatted_start_date = time.strftime(
        "%Y-%m-%d", time.localtime(start_date / 1000))
    formatted_end_date = time.strftime(
        "%Y-%m-%d", time.localtime(end_date / 1000))

    # FullCalendarの表示範囲のみ表示
    events = todolist.objects.filter(
        start_date__lt=formatted_end_date, end_date__gt=formatted_start_date
    )

    # fullcalendarのため配列で返却
    list = []
    for event in events:
        list.append(
            {
                "title": event.title,
                "start": event.start_date,
                "end": event.end_date,
            }
        )

    return JsonResponse(list, safe=False)