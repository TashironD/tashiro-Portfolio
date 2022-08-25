from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic import View
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings

# Create your views here.


class Index(TemplateView):
    template_name="index.html"


class BotApiView(View):
    chatbot=ChatBot(**settings.CHATTERBOT)

    def post(self,request,*args,**kwargs):
        input_data=request.POST.get("input_text")

        if not input_data:
            return HttpResponse("<p>質問を入力してください。</p>",status=400)

        bot_response=self.chatbot.get_response(input_data)

        http_response=HttpResponse()
        http_response.write("{}:{}".format("むさし陶器",bot_response,))
        return http_response