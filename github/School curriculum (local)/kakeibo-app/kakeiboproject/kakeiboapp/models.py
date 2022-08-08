from django.db import models# データベースを使うためのもの

class Record(models.Model):

    title=models.CharField(max_length=100)#文字型上限100
    memo=models.TextField(blank=True,null=True)#テキスト
    type=models.IntegerField(choices=[(0,"収入"),(1,"支出")])#支出か収入かを分ける
    amount=models.IntegerField()#金額を指定する　　整数型
    date=models.DateField()#日付の型

    def __str__(self):
        return self.title