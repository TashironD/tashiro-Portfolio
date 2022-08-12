

import requests#API処理のため
from datetime import datetime,timedelta,timezone#日にち、時間
from bs4 import BeautifulSoup as bs#HTMLを解析する為
import time#サーバーへの負荷を減らすために処理を止めるタイマー


#NEWSAPI
load_url="https://news.yahoo.co.jp/topics/top-picks"#yahooサイトのURL
html=requests.get(load_url)#サイト情報を格納
soup=bs(html.content,"html.parser")#BeautifulSoupでhtmlを解析
topic=soup.find_all("div",class_="newsFeed_item_title")#ニュースタイトルだけを抜き出す
news_mess=""#空のメッセージ変数を作成
#順番にメッセージに追加していく
for erements in topic:
    news_mess+="\n"+"#"+erements.text
#自分で詳細を見にいけるようにURLも記載
news_mess+=load_url


#天気API
#APIをコールする
url ="http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url=url.format(city="Tokyo,jp",key=(openwethermapで取得したkey) # keyには自分のAPIキーを入れる
r=requests.get(url)#requestsで天気情報を取得
data=r.json()#json型に変換

#タイムゾーンの設定
tz=timezone(timedelta(hours=+9),"JST")

#見本標準時に変換・必要な項目を取り出す
wether_mess=""#空のメッセージ変数を作成
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