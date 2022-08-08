from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Customer(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):#__str__:文字列で返す時に使う。
        return self.name


class Sales(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)
    #一対多数のForeignKeyでCustomerクラスと紐づけ、on_delete(PROTECT):deleteされても親データ(Customer)はPROTECTする
    progress=models.IntegerField(choices=[(0,"電話連絡済み"),(1,"訪問済み"),(2,"契約書送付済み"),(3,"契約済み"),(4,"失注")])
    manager_checked=models.BooleanField(default=False)#BooleanFieldは0、1の二択
    memo=models.TextField()
    staff=models.ForeignKey(User,on_delete=models.PROTECT,limit_choices_to={"is_superuser":False})
    #user:管理画面のuserをインポート。 is_superuser:False=superuserは表示しない。

    def __str__(self):
        return self.customer.name