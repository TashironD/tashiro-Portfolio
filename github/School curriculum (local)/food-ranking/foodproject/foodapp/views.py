from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
import requests

myKey=1034011073977272415

class TopView(TemplateView):
    template_name="top.html"

    def get_context_data(sels,**kwargs):
        context=super().get_context_data(**kwargs)

        url=("https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426"
        "?format=json&categoryType=large"
        "&applicationId={RakutenAppKey}")

        url=url.format(RakutenAppKey=#####(楽天のAPIキー)#####
        )
        response=requests.get(url)

        #<!--response=requests.get("https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?format=json&categoryType=large&applicationId=1034011073977272415")

        context["category_list"]=response.json()["result"]["large"]

        return context


class RankingView(TemplateView):
    template_name="ranking.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)

        category_id=self.request.GET.get("category_id")
        
        response=requests.get(
        "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426"
        "?format=json"
        f"&categoryId={category_id}"
        "&applicationId=1034011073977272415")
        
        context["ranking"]=response.json()["result"]
        return context




#def someview(request):
    #return render(request,"top.html",{})


