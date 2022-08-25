from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.ext.django_chatterbot import settings


def training():
    chatbot=ChatBot(**settings.CHATTERBOT)
    trainer=ListTrainer(chatbot)

    trainer.train([
        'こんにちは',
        'どうもこんにちは',
        'おすすめは？',
        '５色の箸置きや、豆皿が人気です。',        
        'マグカップはありますか？',
        '様々なコーヒーマグがあります。ぜひオンラインショップでご覧ください。',
        '新作情報を知りたい',
        'Twitter,Instagram,Facebookで随時お知らせしています。ぜひフォローしてください。',
        '電子レンジは使える？',
        'はい。ただし、銀彩、金彩など金属で上絵付けをしているものはご使用いただくことができません。',
        'オーブンは使える？',
        '耐熱ではないので、オーブンの使用はできません。',
        '実際に見ることはできますか？',
        'オンラインショップのみでの販売となりますが、ライフスタイルショップロクナナでは取り扱いが豊富で、多くの器を直接見ていただけます。住所は、東京都渋谷区神宮前1-1-12、電話番号はxx-xxxx-xxxxです。Webサイトからのお問い合わせも可能です。',
        'さようなら',
        'さようなら。プログラムを終了してください',    
    ])

    trainer.train([
        'こんばんわ',
        'どうもおばんです',])

    trainer.train([
        'おはよう',
        'おはようございます。気分のいい朝に武蔵陶器のマブカップで朝のティータイムはいかがですか？', ])