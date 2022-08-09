

import requests
from datetime import datetime,timedelta,timezone
from bs4 import BeautifulSoup as bs
import time


#NEWSAPI
load_url="https://news.yahoo.co.jp/topics/top-picks"
html=requests.get(load_url)
soup=bs(html.content,"html.parser")
#topic=soup.find("ul",class_="newsFeed_list")
topic=soup.find_all("div",class_="newsFeed_item_title")
news_mess=""
for erements in topic:
    news_mess+="\n"+"#"+erements.text


news_mess+=load_url


#天気API
#APIをコールする
url ="http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url=url.format(city="Tokyo,jp",key=#####(openwethermapで取得したkey)#####
) # keyには自分のAPIキーを入れる
r=requests.get(url)
data=r.json()

#タイムゾーンの設定
tz=timezone(timedelta(hours=+9),"JST")

#見本標準時に変換・必要な項目を取り出す
wether_mess=""
i=0
for dat in data["list"]:
    if i<10:
        jst=datetime.fromtimestamp(dat["dt"],tz)
        jst=str(jst)[-20:-12]+"時"
        
        #天気
        #weather=dat["weather"][0]["main"]
        s=dat["weather"][0]["description"]
        
        #最高気温
        temp_max=dat["main"]["temp_max"]
        temp_max=str(temp_max)[:-1]
        #最低気温
        temp_min=dat["main"]["temp_min"]
        temp_min=str(temp_min)[:-1]
        #湿度℃
        humidity=dat["main"]["humidity"]
        
        wether_mess+=("\n"+"\n"+str(jst)+"\n"+"天気："+str(s)+"\n"+"最高気温："+temp_max+"度"+"\n"+"最低気温："+temp_min+"度"+"\n"+"湿度："+str(humidity)+"%")
        i=i+1
        
    else:
        break




#LINEAPI
#取得したトークン
TOKEN=#####(line-notifyでtokenを取得)#####
#APIのURL
api_url="https://notify-api.line.me/api/notify"
#通知内容
send_news=news_mess
send_wether=wether_mess

#情報を辞書型にする
TOKEN_dic={"Authorization":"Bearer"+" "+TOKEN}
send_news_dic={"message":send_news}
send_wether_dic={"message":send_wether}

#LINE通知を送る（200:成功時　400:リクエストが不正　401:アクセストークンが無効　500:サーバー内エラーによる失敗
requests.post(api_url, headers=TOKEN_dic, data=send_news_dic)

time.sleep(1)

#LINE通知を送る（200:成功時　400:リクエストが不正　401:アクセストークンが無効　500:サーバー内エラーによる失敗
requests.post(api_url, headers=TOKEN_dic, data=send_wether_dic)